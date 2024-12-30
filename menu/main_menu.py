# menu/main_menu.py
from colorama import Fore
from menu.main_menu import main_menu  # นำเข้าฟังก์ชัน main_menu จากไฟล์ main_menu.py

def main_menu():
    print("\nยินดีต้อนรับเข้าสู่ Main Menu")
    print("1. sms")
    print("2. รายการที่ 2")
    print("3. ออกจากระบบ")

    choice = input("กรุณาเลือกตัวเลือก: ")

    if choice == '1':
        print(Fore.CYAN + "คุณเลือก รายการที่ 1")
    elif choice == '2':
        print(Fore.CYAN + "คุณเลือก รายการที่ 2")
    elif choice == '3':
        print(Fore.YELLOW + "ออกจากระบบแล้ว")
        exit()  # ออกจากโปรแกรม
    else:
        print(Fore.RED + "ตัวเลือกไม่ถูกต้อง")
        main_menu()