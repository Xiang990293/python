import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import random

class FFTApp:
    def __init__(self):
        self.stopAnimation = False
        self.AnimatingID = None
        self.points = []
        
        self.root = tk.Tk()
        self.root.title("Draw and Compute FFT")
        
        self.c_width, self.c_height = 800, 800
        
        self.last_x, self.last_y = 0, 0
        
        self.offset_x = 0
        self.offset_y = 0
        self.move_start_x = None
        self.move_start_y = None
        
        self.root_divider = tk.Frame(self.root)
        self.root_divider.pack(fill='both', expand=True, side='bottom')
        self.left_frame = tk.Frame(self.root_divider, width=self.c_width//2)
        self.left_frame.pack(side='left')
        self.right_frame = tk.Frame(self.root_divider, width=self.c_width//2)
        self.right_frame.pack(side='right')
        
        self.canvas = tk.Canvas(self.root, width=self.c_width, height=self.c_height, bg='white')
        self.canvas.pack(side='top')
        
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.center_drawing)
        
        self.btn_fft = tk.Button(self.left_frame, text="Compute FFT", command=self.compute_and_draw_fft)
        self.btn_fft.pack()
        
        self.show_plot_btn = tk.Button(self.left_frame, text="Show FFT Plot", command=lambda: self.plot_fft(*self.fft(np.array([complex(p[0]-self.c_width//2, (p[1]-self.c_height//2)) for p in self.points]))))
        self.show_plot_btn.pack()
        
        self.stop_animation_btn = tk.Button(self.left_frame, text="Stop Animation", command=self.stop_animation)
        self.stop_animation_btn.pack()
        
        self.clear_canvas_btn = tk.Button(self.left_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_canvas_btn.pack()
        
        self.accuracy_setter = tk.Scale(self.right_frame, from_=1, to=99, label="Arrow Count", orient=tk.HORIZONTAL)
        self.accuracy_setter.set(99)
        self.accuracy_setter.pack()
        
        self.root.mainloop()
    
    def get_arrow_count(self):
        return self.accuracy_setter.get()

    def start_drawing(self, event):
        self.move_start_x, self.move_start_y = event.x, event.y
        self.last_x, self.last_y = event.x, event.y
        points = [(event.x, event.y)]
        
    def draw(self, event):
        self.canvas.create_line((self.last_x, self.last_y, event.x, event.y), fill='black', width=2)
        self.last_x, self.last_y = event.x, event.y
        self.points.append((event.x, event.y))
        
    def center_drawing(self, event):
        if not self.points:
            return
        # 計算重心
        xs = [p[0] for p in self.points]
        ys = [p[1] for p in self.points]
        centroid_x = sum(xs) / len(xs)
        centroid_y = sum(ys) / len(ys)

        # 計算偏移量使重心對齊畫布中心
        center_x, center_y = self.c_width // 2, self.c_height // 2
        dx = center_x - centroid_x
        dy = center_y - centroid_y

        # 更新所有點座標（整體平移）
        self.points = [(x + dx, y + dy) for x, y in self.points]

        # 清畫布並以新座標繪製
        self.canvas.delete("all")
        for i in range(1, len(self.points)):
            x1, y1 = self.points[i - 1]
            x2, y2 = self.points[i]
            self.canvas.create_line(x1, y1, x2, y2, fill='black', width=2)

    # 如有動畫，這裡也可以重新啟動動畫、FFT等


    # # create signal
    # fs = 100
    # t = np.arange(0, 1, 1/fs)
    # freq = 5
    # signal = np.sin(2 * np.pi * freq * t)

    def fft(self, signal):
        fft_result = np.fft.fft(signal)
        frequencies = np.fft.fftfreq(len(fft_result), 1/len(fft_result))
        
        return fft_result, frequencies

    def plot_fft(self, fft_result, frequencies):
        fs = len(frequencies)
        plt.bar(frequencies[:fs//2], np.abs(fft_result)[:fs//2])
        plt.yscale('log')
        plt.title('FFT of a 5 Hz Sine Wave')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.show()
        
    def compute_and_draw_fft(self):
        if len(self.points) < 2:
            return

        origin_x, origin_y = self.c_width // 2, self.c_height // 2
        signal = np.array([complex(p[0] - origin_x, p[1] - origin_y) for p in self.points])
        signal = signal - np.mean(signal)  # 扣除重心

        fft_result, fft_frequencies = self.fft(signal)

        arrow_count = self.get_arrow_count()
        self.stopAnimation = False
        scale = 1/len(fft_result)  # 縮放與箭頭數量正比調整

        # 傳入arrow_count控制箭頭數量
        self.animate_arrows(fft_result, fft_frequencies, origin=(origin_x, origin_y), scale=scale,
                            step=0, animation_id=None, arrow_count=arrow_count)


    def animate_arrows(self, fft_res, freqs, origin, scale, step=0, animation_id=None, arrow_count=None):
        if self.stopAnimation:
            return
        elif animation_id is None:
            self.AnimatingID = random.randint(0, 2147483647)
            animation_id = self.AnimatingID
        elif animation_id != self.AnimatingID:
            self.stop_animation()
            return

        self.canvas.delete("arrow")
        N = len(fft_res)
        current_pos = complex(*origin)

        # 只繪製前arrow_count個箭頭
        count = arrow_count if arrow_count is not None else N

        for k in range(min(count, N)):
            if abs(freqs[k]) < 1e-10:  # 忽略頻率0分量
                continue
            freq = freqs[k]
            coef = fft_res[k]
            vector = coef * np.exp(2j * np.pi * freq * step) * scale
            next_pos = current_pos + vector
            self.canvas.create_line(current_pos.real, current_pos.imag, next_pos.real, next_pos.imag,
                                    arrow=tk.LAST, fill='blue', tags="arrow")
            current_pos = next_pos


        # 固定旋轉速度，每秒旋轉速率(rps)，根據呼叫間隔調整step增量
        rotation_speed_rps = 0.2  # 每秒旋轉0.2圈
        update_interval_ms = 50  # 更新間隔 50ms
        step_increment = rotation_speed_rps * update_interval_ms / 1000  # 每更新step增加量

        self.root.after(update_interval_ms, self.animate_arrows, fft_res, freqs, origin, scale,
                        step + step_increment, animation_id, arrow_count)

        
    def stop_animation(self):
        self.stopAnimation = True
        self.AnimatingID = None
        self.canvas.delete("arrow")
        
    
    def clear_canvas(self):
        self.canvas.delete("all")
        self.points = []

if __name__ == "__main__":
    FFTApp = FFTApp()