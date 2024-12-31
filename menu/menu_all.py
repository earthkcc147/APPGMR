from colorama import Fore, Style
import time
import subprocess
import os
from banners import print_logo
import unicodedata


def clear_console():
    # ล้างหน้าจอคอนโซล
    os.system('cls' if os.name == 'nt' else 'clear')


def unicode_length(text):
    """คำนวณความยาวข้อความที่รองรับ Unicode"""
    return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in text)


def menu_all():
    clear_console()

    # แสดงข้อความยินดีต้อนรับ
    print_logo()
    print(Fore.CYAN + Style.BRIGHT + "\nยินดีต้อนรับเข้าสู่ Main Menu\n" + Style.RESET_ALL)

    # รายการตัวเลือกในเมนู แบ่งเป็นกลุ่ม
    menu_options = [
        # กลุ่ม SMS
        ("📨 SMS", "SPAM 42api"),
        ("📧 Gmail", "SPAM Gmail"),
        
        # คั่นกลุ่ม
        ("---", "-----"),
        
        # กลุ่ม Facebook
        ("👥 Facebook", "Message"),
        ("👥 Facebook", "Comment"),
        
        # คั่นกลุ่ม
        ("---", "-----"),
        
        # กลุ่ม Discord
        ("🎭 Discord", "Copy Discord"),
        ("🎭 Discord", "Hack Discord"),
        
        # คั่นกลุ่ม
        ("---", "-----"),
        
        # กลุ่ม IP
        ("🌐 Ip", "ส่ง DDOS & FLOAT1"),
        ("🌐 Ip", "ส่ง DDOS & FLOAT2"),
        
        # คั่นกลุ่ม
        ("---", "-----"),
        
        # กลุ่มอื่นๆ
        ("💥 Gta", "ส่ง DDOS & FLOAT"),
        ("🛠 Tools", "เครื่องมือช่วยเหลือ"),
        ("💻 System", "ข้อมูลระบบ"),
        ("📞 Support", "ช่วยเหลือ"),
        ("❓ Help", "คำถามที่พบบ่อย"),
    ]

    # คำนวณจำนวนแถวและคอลัมน์ให้เหมาะสม
    max_columns = 3  # กำหนดจำนวนคอลัมน์สูงสุด
    num_rows = (len(menu_options) + max_columns - 1) // max_columns  # คำนวณจำนวนแถว

    # วนลูปเพื่อแสดงเมนู
    for row in range(num_rows):
        for col in range(max_columns):
            index = row + col * num_rows
            if index < len(menu_options):
                option = menu_options[index]
                left_text = f"{index + 1:02}. {option[0]}"
                right_text = f"({option[1]})"
                padding = 35 - unicode_length(left_text)  # คำนวณระยะห่าง
                # ตรวจสอบว่าเป็นตัวคั่น (---)
                if option[0] == "---":
                    print(Fore.YELLOW + "-"*35 + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + left_text + Fore.YELLOW + right_text.ljust(padding), end="")
        print()  # จัดให้อยู่ในแถวใหม่

    # เพิ่มตัวเลือกพิเศษ
    print(Fore.RED + "00. ❌ ออกจากระบบ" + Style.RESET_ALL)

    # รับข้อมูลจากผู้ใช้
    choice = input(Fore.BLUE + "กรุณาเลือกตัวเลือก: " + Style.RESET_ALL)

    # ตรวจสอบตัวเลือกที่ผู้ใช้เลือก
    if choice == '1':
        print(Fore.GREEN + "กำลังรันไฟล์ sms.py..." + Style.RESET_ALL)
        subprocess.run(["python3", "function/sms/sms1.py"])
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
        time.sleep(1)
        exit()
    else:
        print(Fore.RED + "ตัวเลือกไม่ถูกต้อง" + Style.RESET_ALL)
        time.sleep(1)
        menu_all()


# เรียกใช้งานฟังก์ชันเมนู
if __name__ == "__main__":
    menu_all()