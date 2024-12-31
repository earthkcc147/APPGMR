import subprocess
import requests
import os
from banners import ip
from colorama import Fore, Back, Style

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')

# เมนู SMS
def show_ip_menu():
    while True:
        clear_console()
        ip()
        print(Fore.CYAN + "\n📱 --- เมนู ddos & float --- 📱" + Style.RESET_ALL)
        print(Fore.GREEN + "1. 📨 message" + Fore.YELLOW + " (ข้อความ) " + Style.RESET_ALL)
        print(Fore.GREEN + "2. 💭 comment" + Fore.YELLOW + " (คอมเม้นท์) " + Style.RESET_ALL)
        print(Fore.YELLOW + "00. 🔙 ย้อนกลับ" + Style.RESET_ALL)

        try:
            sms_choice = int(input(Fore.BLUE + "\n🔔 กรุณาเลือกตัวเลือก: " + Style.RESET_ALL))

            if sms_choice == 00:
                print(Fore.YELLOW + "🔙 กลับสู่เมนูหลัก..." + Style.RESET_ALL)
                from menu import main_menu  # นำเข้า main_menu

                main_menu()  # กลับไปยัง main_menu
                break
            elif sms_choice == 1: 
                print(Fore.GREEN + "กำลังรันไฟล์..." + Style.RESET_ALL)
                subprocess.run(["python3", "function/facebook/message.py"])
            elif sms_choice == 2: 
                print(Fore.GREEN + "กำลังรันไฟล์..." + Style.RESET_ALL)
                subprocess.run(["python3", "function/facebook/message2.py"])


            else:
                print(Fore.RED + "❌ ตัวเลือกไม่ถูกต้อง กรุณาลองอีกครั้ง!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "❌ กรุณากรอกตัวเลขเท่านั้น!" + Style.RESET_ALL)