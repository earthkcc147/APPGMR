import os
from colorama import init, Fore, Style
from function.welcome import print_intro, print_logo
from function.login import login  # นำเข้าฟังก์ชัน login จากไฟล์ login.py

# เริ่มต้นการใช้งาน colorama
init(autoreset=True)

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')


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
        exit()  # ออกจากโปรแกรม
    else:
        print(Fore.RED + "ตัวเลือกไม่ถูกต้อง")
        main_menu()


if __name__ == '__main__':
    clear_console()
    print_intro()
    
    # รอการกด Enter เพื่อดำเนินการต่อ
    input(Fore.GREEN + "\nกด Enter เพื่อดำเนินการต่อ...")

    # เรียกใช้ฟังก์ชัน login และตรวจสอบการล็อคอิน
    if login():
        main_menu()