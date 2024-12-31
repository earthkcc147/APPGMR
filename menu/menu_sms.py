import subprocess
import requests
import os
from banners import sms
from colorama import Fore, Back, Style

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')

# เมนู SMS
def show_sms_menu():
    while True:
        clear_console()
        sms()
        print(Fore.CYAN + "\n📱 --- เมนู SMS --- 📱" + Style.RESET_ALL)
        print(Fore.GREEN + "1. 📨 SMS" + Fore.YELLOW + " (42 API) " + Style.RESET_ALL)
        print(Fore.YELLOW + "00. 🔙 ย้อนกลับ" + Style.RESET_ALL)

        try:
            sms_choice = int(input(Fore.BLUE + "\n🔔 กรุณาเลือกตัวเลือก: " + Style.RESET_ALL))

            if sms_choice == 00:
                print(Fore.YELLOW + "🔙 กลับสู่เมนูหลัก..." + Style.RESET_ALL)
                from menu import main_menu  # นำเข้า main_menu

                main_menu()  # กลับไปยัง main_menu
                break
            elif sms_choice == 1: 
                print(Fore.GREEN + "กำลังรันไฟล์ sms.py..." + Style.RESET_ALL)
                subprocess.run(["python3", "function/sms/sms1.py"])
            else:
                print(Fore.RED + "❌ ตัวเลือกไม่ถูกต้อง กรุณาลองอีกครั้ง!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "❌ กรุณากรอกตัวเลขเท่านั้น!" + Style.RESET_ALL)