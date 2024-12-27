import os
import json
import getpass
from dotenv import load_dotenv
from colorama import init, Fore, Style
from function.welcome import print_intro, print_logo

# เริ่มต้นการใช้งาน colorama
init(autoreset=True)

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
    print("กรุณากรอกข้อมูลสำหรับล็อคอิน")
    username_input = input("Username: ")
    password_input = getpass.getpass("Password: ")

    # ตรวจสอบ username และ password
    if username_input in USERS and USERS[username_input]["password"] == password_input:
        print(Fore.GREEN + "ล็อคอินสำเร็จ")
        main_menu()
    else:
        print(Fore.RED + "ข้อมูลไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")
        login()

def main_menu():
    print("\nยินดีต้อนรับเข้าสู่ Main Menu")
    print("1. รายการที่ 1")
    print("2. รายการที่ 2")
    print("3. ออกจากระบบ")

    choice = input("กรุณาเลือกตัวเลือก: ")

    if choice == '1':
        print(Fore.CYAN + "คุณเลือก รายการที่ 1")
    elif choice == '2':
        print(Fore.CYAN + "คุณเลือก รายการที่ 2")
    elif choice == '3':
        print(Fore.YELLOW + "ออกจากระบบแล้ว")
    else:
        print(Fore.RED + "ตัวเลือกไม่ถูกต้อง")
        main_menu()

if __name__ == '__main__':
    login()
