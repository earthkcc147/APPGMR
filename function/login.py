import os
import json
import getpass
from colorama import Fore, Back, Style, init
from dotenv import load_dotenv
from function.welcome import print_intro, print_logo, print_login
from function.send.disget import smdc, get_current_time, send

# เริ่มต้นการใช้งาน colorama
init(autoreset=True)

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึงข้อมูล USERS จาก .env
USERS_JSON = os.getenv("USERS")
current_time = get_current_time()

# แปลงข้อมูล USERS_JSON เป็น dictionary
try:
    users_data = json.loads(USERS_JSON)
except json.JSONDecodeError:
    print(Fore.RED + "ไม่สามารถแปลงข้อมูล USERS จาก .env ได้ ❌")
    exit()

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')


def login():
    print_login()
    print(Fore.CYAN + "กรุณากรอกข้อมูลสำหรับล็อคอิน หรือพิมพ์ 'exit' เพื่อลงจากระบบ")

    username_input = input(Fore.YELLOW + "Username: ")
    if username_input.lower() == 'exit':
        clear_console()
        print(Fore.YELLOW + "ออกจากระบบแล้ว 🚪")
        exit()

    password_input = getpass.getpass(Fore.YELLOW + "Password: ")
    if password_input.lower() == 'exit':
        clear_console()
        print(Fore.YELLOW + "ออกจากระบบแล้ว 🚪")
        exit()

    # ตรวจสอบ username และ password
    if username_input in users_data and users_data[username_input]["password"] == password_input:
        clear_console()
        print(Fore.GREEN + "ล็อคอินสำเร็จ ✅")
        print(Fore.GREEN + "ยินดีต้อนรับ, " + username_input + " 🎉")
        send(username_input)  # ใช้ username_input แทน username
        return True
    else:
        print(Fore.RED + "ข้อมูลไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง ❌")
        return False