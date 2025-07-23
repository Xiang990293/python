import cv2
import numpy as np
import imagehash
import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
CONFIG_FILE = "config.json"


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "default_folder": "",
        "delete_corrupted": False,
        "hash_threshold": 5,
        "similarity_threshold": 0.85,
        "exact_match_threshold": 0.98
    }


def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def calc_similarity(img1_path, img2_path):
    try:
        img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
        if img1 is None or img2 is None:
            return 0.0
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        return max_val
    except Exception as e:
        print(f"[calc_similarity] Error comparing {img1_path} and {img2_path}: {e}")
        return 0.0


def list_images(folder):
    exts = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    try:
        return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(exts)]
    except Exception as e:
        print(f"[list_images] 無法讀取資料夾 {folder}: {e}")
        return []


def group_by_hash(images, hashfunc=imagehash.phash, threshold=5, delete_corrupted=False):
    groups = []
    hashes = []
    for img_path in images:
        try:
            h = hashfunc(Image.open(img_path))
        except Exception as e:
            print(f"[group_by_hash] 開啟圖片失敗 {img_path}: {e}")
            if delete_corrupted:
                try:
                    os.remove(img_path)
                    print(f"已自動刪除損壞圖片: {img_path}")
                except Exception as e2:
                    print(f"刪除失敗 {img_path}: {e2}")
            continue
        matched_group = None
        for i, gh in enumerate(hashes):
            if abs(h - gh) <= threshold:
                matched_group = i
                break
        if matched_group is not None:
            groups[matched_group].append(img_path)
        else:
            groups.append([img_path])
            hashes.append(h)
    return [g for g in groups if len(g) > 1]


class ConfigGUI:
    def __init__(self, root, config, callback):
        self.root = root
        self.config = config
        self.callback = callback
        root.title("設定 - 相似照片清理")

        tk.Label(root, text="預設照片資料夾:").grid(row=0, column=0, sticky="e")
        self.folder_var = tk.StringVar(value=config.get("default_folder", ""))
        tk.Entry(root, textvariable=self.folder_var, width=40).grid(row=0, column=1)
        tk.Button(root, text="選擇...", command=self.choose_folder).grid(row=0, column=2)

        self.dc_var = tk.BooleanVar(value=config.get("delete_corrupted", False))
        tk.Checkbutton(root, text="自動刪除損壞圖片", variable=self.dc_var).grid(row=1, column=1, sticky="w")

        tk.Label(root, text="哈希閾值 (整數):").grid(row=2, column=0, sticky="e")
        self.hash_var = tk.IntVar(value=config.get("hash_threshold", 5))
        tk.Entry(root, textvariable=self.hash_var).grid(row=2, column=1)

        tk.Label(root, text="高度相似度閾值 (0~1):").grid(row=3, column=0, sticky="e")
        self.sim_var = tk.DoubleVar(value=config.get("similarity_threshold", 0.85))
        tk.Entry(root, textvariable=self.sim_var).grid(row=3, column=1)

        tk.Label(root, text="完全相似度閾值 (0~1):").grid(row=4, column=0, sticky="e")
        self.exact_var = tk.DoubleVar(value=config.get("exact_match_threshold", 0.98))
        tk.Entry(root, textvariable=self.exact_var).grid(row=4, column=1)

        tk.Button(root, text="儲存", command=self.save).grid(row=5, column=0)
        tk.Button(root, text="取消", command=root.quit).grid(row=5, column=1)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_var.set(folder)

    def save(self):
        try:
            self.config["default_folder"] = self.folder_var.get()
            self.config["delete_corrupted"] = self.dc_var.get()
            self.config["hash_threshold"] = self.hash_var.get()
            self.config["similarity_threshold"] = self.sim_var.get()
            self.config["exact_match_threshold"] = self.exact_var.get()
            save_config(self.config)
            messagebox.showinfo("成功", "設定已儲存")
            self.root.destroy()
            if self.callback:
                self.callback()
        except Exception as e:
            messagebox.showerror("錯誤", f"儲存設定失敗: {e}")


class ImageCompareApp(tk.Toplevel):
    def __init__(self, master, img1_path, img2_path, similarity):
        super().__init__(master)
        self.title("相似照片比較")
        self.img1_path = img1_path
        self.img2_path = img2_path
        self.similarity = similarity

        # 載入並縮放圖片
        img1 = Image.open(img1_path).resize((300, 300))
        img2 = Image.open(img2_path).resize((300, 300))
        self.tk_img1 = ImageTk.PhotoImage(img1)
        self.tk_img2 = ImageTk.PhotoImage(img2)

        # 排版圖片與標題
        tk.Label(self, text=os.path.basename(img1_path)).grid(row=0, column=0)
        tk.Label(self, text=os.path.basename(img2_path)).grid(row=0, column=1)
        tk.Label(self, image=self.tk_img1).grid(row=1, column=0)
        tk.Label(self, image=self.tk_img2).grid(row=1, column=1)
        tk.Label(self, text=f"相似度: {similarity:.3f}").grid(row=2, column=0, columnspan=2)

        # 按鈕操作
        tk.Button(self, text="刪除左邊", command=lambda: self.delete_and_close(img1_path)).grid(row=3, column=0)
        tk.Button(self, text="刪除右邊", command=lambda: self.delete_and_close(img2_path)).grid(row=3, column=1)
        tk.Button(self, text="保留", command=self.destroy).grid(row=4, column=0, columnspan=2)

    def delete_and_close(self, path):
        try:
            os.remove(path)
            messagebox.showinfo("刪除成功", f"已刪除 {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("刪除失敗", f"刪除檔案時出錯: {e}")
        self.destroy()


class GroupListApp:
    def __init__(self, root, config):
        self.root = root
        self.config = config
        self.root.title("相似照片清理 - 相似照片群組")
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        # 按鈕列
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill="x")
        tk.Button(btn_frame, text="重新選擇資料夾", command=self.select_folder).pack(side="left")
        tk.Button(btn_frame, text="重新掃描", command=self.scan_images).pack(side="left")
        tk.Button(btn_frame, text="設定", command=self.open_config).pack(side="left")
        tk.Button(btn_frame, text="結束", command=root.quit).pack(side="right")

        self.folder = config.get("default_folder", "")
        self.groups = []
        self.images = []

        # Listbox 顯示群組
        self.listbox = tk.Listbox(self.frame, width=80, height=20)
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<Double-Button-1>", self.on_group_double_click)

        # 捲動條
        scrollbar = tk.Scrollbar(self.frame, command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.scan_images()

    def open_config(self):
        def reload_after_save():
            self.folder = self.config.get("default_folder", "")
            self.scan_images()
        win = tk.Toplevel(self.root)
        ConfigGUI(win, self.config, reload_after_save)

    def select_folder(self):
        folder = filedialog.askdirectory(initialdir=self.folder or None)
        if folder:
            self.folder = folder
            self.scan_images()

    def scan_images(self):
        self.images = list_images(self.folder)
        self.groups = group_by_hash(self.images,
                                    threshold=self.config.get("hash_threshold", 5),
                                    delete_corrupted=self.config.get("delete_corrupted", False))
        self.listbox.delete(0, tk.END)
        if not self.groups:
            self.listbox.insert(tk.END, "無找到相似照片群組")
            return
        for i, group in enumerate(self.groups):
            self.listbox.insert(tk.END, f"[群組{i+1}] 共{len(group)}張疑似相似照片")

    def on_group_double_click(self, event):
        sel = self.listbox.curselection()
        if not sel or not self.groups:
            return
        idx = sel[0]
        group = self.groups[idx]
        # 計算兩兩相似度，找最高配對做比較展示
        n = len(group)
        sim_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(i + 1, n):
                sim_matrix[i, j] = calc_similarity(group[i], group[j])
                sim_matrix[j, i] = sim_matrix[i, j]

        max_idx = np.unravel_index(np.argmax(sim_matrix, axis=None), sim_matrix.shape)
        img_a = group[max_idx[0]]
        img_b = group[max_idx[1]]
        sim = sim_matrix[max_idx]

        if sim < self.config.get("similarity_threshold", 0.85):
            messagebox.showinfo("提示", "這組照片中找不到高於相似度閾值的照片對")
            return

        # 呼叫圖片比較器
        ImageCompareApp(self.root, img_a, img_b, sim)


def main():
    config = load_config()
    root = tk.Tk()
    root.geometry("700x400")
    app = GroupListApp(root, config)
    root.mainloop()


if __name__ == "__main__":
    main()
