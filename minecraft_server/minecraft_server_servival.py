#!/usr/bin/env python3
import os
import subprocess
import time
import shutil
import zipfile
import requests
import json
from datetime import datetime
from pathlib import Path
import re


class MinecraftServerManager:
    def __init__(self):
        self.server_dir = Path(
            "/home/xiang990293/Documents/rippou_ripple_researcher/server"
        )
        self.backup_dir = Path("/mnt/sda1/研究維度備份/")
        self.backup_dir.mkdir(exist_ok=True)
        self.min_backup_interval = 6000  # 10分鐘
        self.minecraft_version = "26.1"
        os.chdir(self.server_dir)

    def get_minecraft_version(self, target_dir=None):
        """執行 fabric-installer 取得最新版本，並將檔案放到指定資料夾"""
        if target_dir is None:
            target_dir = self.server_dir / "new_version"
            target_dir.mkdir(exist_ok=True)

        print(f"🔍 在 {target_dir} 執行 fabric-installer 偵測版本...")
        # 執行 fabric-installer，指定輸出目錄
        cmd = [
            "java",
            "-jar",
            "fabric-installer-1.1.1.jar",
            "server",
            "-dir",
            str(target_dir),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)

        # 從輸出中提取版本號
        match = re.search(r"\(([^)]+)\)", result.stdout)
        version = match.group(1) if match else self.minecraft_version
        
        if version == self.minecraft_version:
            print(f"版本仍為: {version}")
        else:
            print(f"檢測到最新版本: {version}")
        
        return version, target_dir

    def download_server_jar(self, version):
        """下載 Minecraft server.jar"""
        print(f"下載 Minecraft {version} server.jar...")
        version_json = requests.get(
            "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        ).json()
        version_url = next(
            (v["url"] for v in version_json["versions"] if v["id"] == version), None
        )

        if version_url:
            download_json = requests.get(version_url).json()
            download_url = download_json["downloads"]["server"]["url"]
            r = requests.get(download_url)
            with open("server.jar", "wb") as f:
                f.write(r.content)
            print("✅ 下載完成")

    def smart_backup(self, version):
        """智慧備份：10分鐘內不重複"""
        now = time.time()
        backups = list(self.backup_dir.glob(f"world_archive_{version}_*.zip"))

        if backups:
            latest_backup = max(backups, key=os.path.getmtime)
            if now - os.path.getmtime(latest_backup) < self.min_backup_interval:
                print("⏰ 10分鐘內已備份，跳過")
                return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.backup_dir / f"world_archive_{version}_{timestamp}.zip"
        with zipfile.ZipFile(backup_file, "w", zipfile.ZIP_DEFLATED) as zf:
            for file in Path("world").rglob("*"):
                zf.write(file, file.relative_to(self.server_dir))
        print("💾 備份完成")

    def update_mods(self, version):
        """檢查並更新模組"""
        print("🔍 檢查模組更新...")
        cmd = ["python3", "-", "-v", version, "-l", "fabric", "-c", "c4NgnwuN", "-u"]
        script = requests.get(
            "https://raw.githubusercontent.com/aayushdutt/modrinth-collection-downloader/master/main.py"
        ).text
        result = subprocess.run(cmd, input=script, capture_output=True, text=True)
        print("✅ 模組更新完成" if result.returncode == 0 else "⚠️ 模組更新有警告")

    def start_server(self):
        """啟動伺服器"""
        java_home = "/home/xiang990293/.sdkman/candidates/java/current/bin/java"
        cmd = [
            java_home,
            "-Xms1G",
            "-Xmx8G",
            "-jar",
            "fabric-server-launch.jar",
            "--nogui",
        ]
        print("🚀 啟動伺服器...")
        subprocess.run(cmd)

    def check_mods_are_latest_for_version(self, minecraft_version):
        """檢查 Collection 中所有模組是否都有指定 Minecraft 版本的支援"""
        print(f"🔍 檢查模組是否支援 {minecraft_version}...")
        
        # 取得 Collection 資訊
        collection_url = "https://api.modrinth.com/v2/project/c4NgnwuN/collection"
        collection = requests.get(collection_url).json()
        
        mods_dir = Path("mods")
        mods_dir.mkdir(exist_ok=True)
        
        unsupported_count = 0
        total_projects = len(collection.get("projects", []))
        
        for project in collection.get("projects", []):
            project_id = project["id"]
            project_title = project["title"]
            
            # 檢查此模組是否有 minecraft_version + Fabric 版本
            versions_url = f'https://api.modrinth.com/v2/project/{project_id}/version?loaders=["fabric"]&game_versions=["{minecraft_version}"]'
            versions = requests.get(versions_url).json()
            
            if versions:  # 有版本 = 支援
                print(f"✅ {project_title}: 支援 {minecraft_version}")
            else:
                print(f"❌ {project_title}: 不支援 {minecraft_version}")
                unsupported_count += 1
        
        print(f"檢查完成: {total_projects - unsupported_count}/{total_projects} 個模組支援 {minecraft_version}")
        
        # 只要有 1 個模組不支援就 False
        return unsupported_count == 0

    def run(self):
        """新的主邏輯：先檢查模組 → 全部最新才更新"""
        while True:
            try:
                # 1. 取得最新 Minecraft 版本
                new_minecraft_version, version_dir = self.get_minecraft_version()

                # 2. **關鍵檢查：模組是否全部都是最新？**
                if self.check_mods_are_latest_for_version(new_minecraft_version):
                    print("🎉 所有模組都是最新版本，執行完整更新！")

                    # 全部最新 → 安全更新 server.jar + fabric-launcher + mods
                    self.download_server_jar(new_minecraft_version)
                    self.update_mods(new_minecraft_version)

                else:
                    print("⚠️  有些模組不是最新，跳過伺服器更新")

                # 3. 智慧備份
                self.smart_backup(new_minecraft_version)

                # 4. 啟動伺服器（不論更新與否）
                self.start_server()

                print("💤 伺服器停止，10秒後重啟...")
                time.sleep(10)

            except KeyboardInterrupt:
                print("🛑 手動停止")
                break

            except Exception as e:
                print(f"❌ 錯誤: {e}")
                time.sleep(30)


if __name__ == "__main__":
    manager = MinecraftServerManager()
    manager.run()
