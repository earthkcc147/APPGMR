from colorama import Fore, Style
import time
import os
import unicodedata
from banners import print_logo


def clear_console():
    """ล้างหน้าจอคอนโซล"""
    os.system('cls' if os.name == 'nt' else 'clear')


def unicode_length(text):
    """คำนวณความยาวข้อความที่รองรับ Unicode"""
    length = 0
    for char in text:
        if unicodedata.east_asian_width(char) in 'WF':  # W = Wide, F = Full-width
            length += 2
        else:
            length += 1
    return length


def align_text(left_text, right_text, fixed_width):
    """จัดข้อความให้ตรงโดยใช้ความกว้าง Unicode"""
    left_length = unicode_length(left_text)
    right_length = unicode_length(right_text)
    padding = fixed_width - (left_length + right_length)
    return left_text + ' ' * max(padding, 0) + right_text


def menu_all():
    clear_console()

    # แสดงข้อความยินดีต้อนรับ
    print_logo()
    print(Fore.CYAN + Style.BRIGHT + "\nยินดีต้อนรับเข้าสู่ Main Menu\n" + Style.RESET_ALL)

    # รายการตัวเลือกในเมนู
    menu_options = [
        ("📨 SMS", "ส่งข้อความ SMS"),
        ("📧 Email", "ส่งอีเมล"),
        ("👥 Facebook", "ส่ง message"),
        ("🎭 Discord", "ส่ง DDOS & FLOAT"),
        ("🌐 Ip", "ส่ง DDOS & FLOAT"),
        ("💥 Gta", "ส่ง DDOS & FLOAT"),
        ("🔐 VPN", "จัดการ VPN"),
        ("🛠 Tools", "เครื่องมือช่วยเหลือ"),
        ("📊 Analytics", "วิเคราะห์ข้อมูล"),
        ("🔍 Search", "ค้นหา"),
        ("🔔 Notifications", "การแจ้งเตือน"),
        ("⚙ Settings", "ตั้งค่าระบบ"),
        ("🖥 Dashboard", "แสดงข้อมูลรวม"),
        ("📂 Files", "จัดการไฟล์"),
        ("🔒 Security", "จัดการความปลอดภัย"),
        ("💻 System", "ข้อมูลระบบ"),
        ("🎮 Games", "เกม"),
        ("🎨 Themes", "ธีม"),
        ("📞 Support", "ช่วยเหลือ"),
        ("❓ Help", "คำถามที่พบบ่อย"),
    ]

    # กำหนดจำนวนแถวต่อคอลัมน์และระยะห่าง
    rows_per_column = 10
    fixed_width = 35  # ความกว้างคงที่ของแต่ละคอลัมน์
    columns = -(-len(menu_options) // rows_per_column)

    # วนลูปเพื่อแสดงเมนู
    for row in range(rows_per_column):
        for col in range(columns):
            index = row + col * rows_per_column
            if index < len(menu_options):
                option = menu_options[index]
                left_text = f"{index + 1:02}. {option[0]}"
                right_text = f"({option[1]})"
                print(Fore.GREEN + align_text(left_text, right_text, fixed_width), end="")
        print()  # จัดให้อยู่ในแถวใหม่

    # เพิ่มตัวเลือกพิเศษ
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
        time.sleep(1)
        exit()
    else:
        print(Fore.RED + "ตัวเลือกไม่ถูกต้อง" + Style.RESET_ALL)
        time.sleep(1)
        menu_all()


# เรียกใช้งานฟังก์ชันเมนู
if __name__ == "__main__":
    menu_all()