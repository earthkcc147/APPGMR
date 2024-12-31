import os
import sys
import subprocess
import requests

# กำหนดชื่อไฟล์ Python ที่จะสร้าง .exe
script_name = "button.py"

# คำสั่งสำหรับการสร้างไฟล์ .exe
def create_exe():
    try:
        # ใช้ PyInstaller สร้างไฟล์ .exe
        subprocess.run(['pyinstaller', '--onefile', '--noconsole', script_name], check=True)

        # ตรวจสอบว่าไฟล์ .exe ถูกสร้างสำเร็จหรือไม่
        exe_file = f'dist/{script_name.replace(".py", ".exe")}'
        if os.path.exists(exe_file):
            print(f"ไฟล์ .exe ถูกสร้างสำเร็จ: {exe_file}")
            # รับ Webhook URL จากผู้ใช้
            discord_webhook_url = input("กรุณากรอก Webhook URL ของ Discord: ")
            # ส่งไฟล์ .exe ไปที่ Discord
            send_to_discord(exe_file, discord_webhook_url)
            # ลบไฟล์ .exe หลังจากส่งไปที่ Discord
            os.remove(exe_file)
            print(f"ไฟล์ .exe ถูกลบแล้ว: {exe_file}")
        else:
            print("ไม่สามารถสร้างไฟล์ .exe ได้")
    except subprocess.CalledProcessError as e:
        print(f"เกิดข้อผิดพลาดในการสร้างไฟล์ .exe: {e}")

# ฟังก์ชันส่งไฟล์ .exe ไปยัง Discord
def send_to_discord(file_path, discord_webhook_url):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {'content': 'ไฟล์ .exe ถูกสร้างเรียบร้อยแล้ว'}
            try:
                response = requests.post(discord_webhook_url, data=data, files=files)
                if response.status_code == 204:
                    print("ไฟล์ .exe ส่งไปที่ Discord เรียบร้อยแล้ว")
                else:
                    print(f"เกิดข้อผิดพลาดในการส่งไฟล์ไปที่ Discord: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"เกิดข้อผิดพลาดในการส่งคำขอ: {e}")
    else:
        print("ไม่พบไฟล์ .exe ที่จะส่งไปยัง Discord")

if __name__ == "__main__":
    create_exe()