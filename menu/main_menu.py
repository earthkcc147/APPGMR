# menu/main_menu.py
from colorama import Fore
from menu.menu_sms import show_sms_menu  

def main_menu():
    print("\nยินดีต้อนรับเข้าสู่ Main Menu")
    print("1. sms")
    print("2. รายการที่ 2")
    print("3. ออกจากระบบ")

    choice = input("กรุณาเลือกตัวเลือก: ")

    if choice == '1':
        show_sms_menu()
    elif choice == '2':
        print(Fore.CYAN + "คุณเลือก รายการที่ 2")
    elif choice == '3':
        print(Fore.YELLOW + "ออกจากระบบแล้ว")
        exit()  # ออกจากโปรแกรม
    else:
        print(Fore.RED + "ตัวเลือกไม่ถูกต้อง")
        main_menu()