import smtplib
import time
import json
import os

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')

clear_console()

# แสดงข้อความ
print("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              โดย @everydaycodings                  \033[1;m")
print("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|              สร้างด้วยโค้ด             \033[1;m")
print("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

# เมนูหลัก
def main_menu():
    print("\nเลือกตัวเลือก:")
    print("1. ใช้ข้อมูลจากไฟล์ email.json")
    print("2. กรอกอีเมลเอง (ส่งแค่ 1 อีเมล)")
    choice = input("กรุณาเลือกตัวเลือก (1/2): ")

    if choice == '1':
        use_json()
    elif choice == '2':
        send_single_email()
    else:
        print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")
        main_menu()

# ฟังก์ชันเพื่อใช้ข้อมูลจากไฟล์ email.json
def use_json():
    email_json_path = 'function/email/email.json'

    # ตรวจสอบว่าไฟล์ email.json มีอยู่หรือไม่
    if not os.path.exists(email_json_path):
        # ถ้าไม่มีไฟล์ ให้สร้างขึ้นมาใหม่
        print(f"ไฟล์ {email_json_path} ไม่มีอยู่ กำลังสร้างไฟล์ใหม่...")
        email_data = {
            "emails": [
                "example1@example.com",
                "example2@example.com",
                "example3@example.com"
            ]
        }
        
        # สร้างไฟล์ email.json และเขียนข้อมูลลงไป
        os.makedirs(os.path.dirname(email_json_path), exist_ok=True)
        with open(email_json_path, 'w') as f:
            json.dump(email_data, f, indent=4)

    # เปิดไฟล์ email.json และโหลดข้อมูล
    with open(email_json_path, 'r') as f:
        data = json.load(f)

    # รับข้อมูลจากผู้ใช้
    email = input("กรุณากรอกที่อยู่อีเมลของคุณ (gmail): ")
    password = input("กรุณากรอกรหัสผ่านของอีเมลของคุณ: ")
    message = input("กรุณากรอกข้อความที่จะส่ง: ")
    message_relode = int(input("คุณต้องการส่งข้อความจำนวนกี่ครั้ง?: "))

    # ลูปเพื่อส่งอีเมล
    for bomb_email in data['emails']:
        for x in range(0, message_relode):
            try:
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login(email, password)
                mail.sendmail(email, bomb_email, message)
                print(f"ส่งข้อความไปยัง {bomb_email}")
                mail.close()
            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการส่งอีเมลไปยัง {bomb_email}: {e}")
            time.sleep(1)

    print("ส่งข้อความเสร็จเรียบร้อย")

# ฟังก์ชันเพื่อกรอกอีเมลเอง
def send_single_email():
    # รับข้อมูลจากผู้ใช้
    email = input("กรุณากรอกที่อยู่อีเมลของคุณ (gmail): ")
    password = input("กรุณากรอกรหัสผ่านของอีเมลของคุณ: ")
    recipient_email = input("กรุณากรอกอีเมลที่ต้องการส่งไป: ")
    message = input("กรุณากรอกข้อความที่จะส่ง: ")

    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        mail.sendmail(email, recipient_email, message)
        print(f"ส่งข้อความไปยัง {recipient_email}")
        mail.close()
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการส่งอีเมลไปยัง {recipient_email}: {e}")

    print("ส่งข้อความเสร็จเรียบร้อย")

# เรียกใช้งานเมนูหลัก
main_menu()