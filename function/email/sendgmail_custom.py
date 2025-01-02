#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, from_password, to_addr):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # ใช้พอร์ต 587
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(from_addr, from_password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.close()
        print("ส่งอีเมลสำเร็จ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    gmail_login = input("กรุณากรอก Gmail ของคุณ: ")
    gmail_password = input("กรุณากรอกรหัสผ่าน Gmail ของคุณ: ")
    subject = input("กรุณากรอกหัวข้อของอีเมล: ")
    message = input("กรุณากรอกข้อความของอีเมล: ")
    to_address = input("กรุณากรอกที่อยู่อีเมลผู้รับ: ")
    send_email(subject, message, from_addr=gmail_login, from_password=gmail_password, to_addr=to_address)