import smtplib
import time
import json

print("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              โดย @everydaycodings                  \033[1;m")
print("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|              สร้างด้วยโค้ด             \033[1;m")
print("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

# เปิดไฟล์ email.json และโหลดข้อมูล
with open('email.json', 'r') as f:
    data = json.load(f)

# รับข้อมูลจากผู้ใช้
email = input("กรุณากรอกที่อยู่อีเมลของคุณ (gmail): ")
password = input("กรุณากรอกรหัสผ่านของอีเมลของคุณ: ")
message = input("กรุณากรอกข้อความที่จะส่ง: ")
message_relode = int(input("คุณต้องการส่งข้อความจำนวนกี่ครั้ง?: "))

# ลูปเพื่อส่งอีเมล
for bomb_email in data['emails']:
    for x in range(0, message_relode):
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        mail.sendmail(email, bomb_email, message)
        print("ส่งข้อความไปยัง {}".format(bomb_email))
    time.sleep(1)

# ปิดการเชื่อมต่อ
mail.close()

print("ส่งข้อความเสร็จเรียบร้อย")