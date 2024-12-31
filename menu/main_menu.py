from colorama import Fore, Back, Style
import time
import os
from banners import print_intro, print_logo, print_login



def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')


def main_menu():
    clear_console()

    # แสดงข้อความยินดีต้อนรับ
    print_logo()
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "\nยินดีต้อนรับเข้าสู่ Main Menu" + Style.RESET_ALL)

    print(Fore.GREEN + "1. 📨 SMS" + Fore.YELLOW + " (ส่งข้อความ SMS)" + Style.RESET_ALL)

    print(Fore.GREEN + "2. 📧 Email" + Fore.YELLOW + " (ส่งอีเมล)" + Style.RESET_ALL)

    print(Fore.GREEN + "3. 👥 Facebook" + Fore.YELLOW + " (Facebook Tools)" + Style.RESET_ALL)

    print(Fore.GREEN + "4. 🎭 Discord" + Fore.YELLOW + " (Discord Tools)" + Style.RESET_ALL)
    
    print(Fore.GREEN + "5. 🌐 Ip" + Fore.YELLOW + " (ส่ง DDOS & FLOAT)" + Style.RESET_ALL)

    print(Fore.GREEN + "6. 💥 Gta" + Fore.YELLOW + " (ส่ง DDOS & FLOAT)" + Style.RESET_ALL)

    print(Fore.RED + "00. ❌ ออกจากระบบ" + Style.RESET_ALL)


    # รับข้อมูลจากผู้ใช้
    choice = input(Fore.BLUE + "กรุณาเลือกตัวเลือก: " + Style.RESET_ALL)

    # ตรวจสอบตัวเลือกที่ผู้ใช้เลือก
    if choice == '1':
        from menu import show_sms_menu
        show_sms_menu()
    elif choice == '2':
        from menu import show_email_menu
        show_email_menu()
    elif choice == '3':
        from menu import show_facebook_menu
        show_facebook_menu()
    elif choice == '4':
        from menu import show_discord_menu
        show_discord_menu()
    elif choice == '5':
        from menu import show_ip_menu
        show_ip_menu()

    elif choice == '00':
        print(Fore.YELLOW + "ออกจากระบบแล้ว" + Style.RESET_ALL)
        time.sleep(1)  # ให้เวลาแสดงข้อความก่อนออก
        exit()  # ออกจากโปรแกรม
    else:
        print(Fore.RED + "ตัวเลือกไม่ถูกต้อง" + Style.RESET_ALL)
        time.sleep(1)  # ให้เวลาแสดงข้อความก่อนแสดงเมนูใหม่
        main_menu()