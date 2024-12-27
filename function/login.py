import os
import json
import getpass
from colorama import Fore
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึงข้อมูล USERS จาก .env
USERS_JSON = os.getenv('USERS')

# ตรวจสอบและแปลงข้อมูล USERS
try:
    USERS = json.loads(USERS_JSON)
except json.JSONDecodeError:
    print(Fore.RED + "ไม่สามารถแปลงข้อมูล USERS จาก .env ได้ ❌")
    exit()

def login():
    print("กรุณากรอกข้อมูลสำหรับล็อคอิน หรือพิมพ์ 'exit' เพื่อลงจากระบบ")
    
    username_input = input("Username: ")
    if username_input.lower() == 'exit':
        print(Fore.YELLOW + "ออกจากระบบแล้ว")
        exit()

    password_input = getpass.getpass("Password: ")
    if password_input.lower() == 'exit':
        print(Fore.YELLOW + "ออกจากระบบแล้ว")
        exit()

    # ตรวจสอบ username และ password
    if username_input in USERS and USERS[username_input]["password"] == password_input:
        print(Fore.GREEN + "ล็อคอินสำเร็จ")
        return True
    else:
        print(Fore.RED + "ข้อมูลไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")
        return False