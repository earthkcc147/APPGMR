#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

GMAIL_LOGIN = 'myemail@gmail.com'
GMAIL_PASSWORD = 'password'

def send_email(subject, message, from_addr=GMAIL_LOGIN, to_addr=''):
    if not to_addr:
        to_addr = input("กรุณากรอกที่อยู่อีเมลผู้รับ: ")  # ถ้าผู้ใช้ไม่ได้ระบุที่อยู่อีเมล ให้ถามผู้ใช้

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    server = smtplib.SMTP('smtp.gmail.com', 587)  # port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(GMAIL_LOGIN, GMAIL_PASSWORD)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.close()

if __name__ == "__main__":
    subject = input("กรุณากรอกหัวข้อของอีเมล: ")
    message = input("กรุณากรอกข้อความของอีเมล: ")
    to_address = input("กรุณากรอกที่อยู่อีเมลผู้รับ: ")
    send_email(subject, message, to_addr=to_address)