import os
from colorama import init, Fore, Style
from banners import print_intro, print_logo
from function import login  # นำเข้าฟังก์ชัน login จากไฟล์ login.py
from menu import main_menu  # นำเข้าฟังก์ชัน main_menu จากไฟล์ main_menu.py


# เริ่มต้นการใช้งาน colorama
init(autoreset=True)

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')


if __name__ == '__main__':
    clear_console()
    print_intro()

    # รอการกด Enter เพื่อดำเนินการต่อ
    input(Fore.GREEN + "\nกด Enter เพื่อดำเนินการต่อ...")
    clear_console()
    main_menu()

    # เรียกใช้ฟังก์ชัน login และตรวจสอบการล็อคอิน
    # if login():
        # main_menu()  # เรียกใช้ฟังก์ชัน main_menu