import pytube
import colorama
import sys
import os

red = colorama.Fore.RED
light_green = colorama.Fore.LIGHTGREEN_EX
green = colorama.Fore.GREEN

print(green, '''
 █████ █████     █████                                     ████                         █████                   
░░███ ░░███     ░░███                                     ░░███                        ░░███                    
 ░░███ ███    ███████   ██████  █████ ███ █████ ████████   ░███   ██████   ██████    ███████   ██████  ████████ 
  ░░█████    ███░░███  ███░░███░░███ ░███░░███ ░░███░░███  ░███  ███░░███ ░░░░░███  ███░░███  ███░░███░░███░░███
   ░░███    ░███ ░███ ░███ ░███ ░███ ░███ ░███  ░███ ░███  ░███ ░███ ░███  ███████ ░███ ░███ ░███████  ░███ ░░░ 
    ░███    ░███ ░███ ░███ ░███ ░░███████████   ░███ ░███  ░███ ░███ ░███ ███░░███ ░███ ░███ ░███░░░   ░███     
    █████   ░░████████░░██████   ░░████░████    ████ █████ █████░░██████ ░░████████░░████████░░██████  █████    
   ░░░░░     ░░░░░░░░  ░░░░░░     ░░░░ ░░░░    ░░░░ ░░░░░ ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░     
   
        ''')

# กำหนดโฟลเดอร์สำหรับบันทึกไฟล์
save_path = os.path.join(os.getcwd(), 'VDO')  # ใช้ os.getcwd() เพื่อหาตำแหน่งของไฟล์ main.py และสร้างโฟลเดอร์ VDO ที่ตำแหน่งเดียวกัน

# ตรวจสอบว่าโฟลเดอร์ VDO มีอยู่หรือไม่ ถ้าไม่มีให้สร้าง
if not os.path.exists(save_path):
    os.makedirs(save_path)

# รับ URL จาก input
url = input("กรุณากรอก URL ของ YouTube: ").strip()

try:
    if url:
        outpath = save_path  # ตั้งค่าให้บันทึกในโฟลเดอร์ VDO

        if "youtube." in url:
            try:
                yt = pytube.YouTube(url)
                yt.streams.get_highest_resolution().download(outpath)  # ดาวน์โหลดวิดีโอที่มีความละเอียดสูงที่สุด
                print(light_green, "ดาวน์โหลดวิดีโอสำเร็จ:", 'ชื่อ: ', yt.title)
                print(light_green, "ดาวน์โหลด:", "\"", yt.title, ".mp4\"", "ไปยัง ", outpath)
            except Exception as error:
                print(red, "เกิดข้อผิดพลาด: ", green, type(error).__name__, "–", error)
        else:
            print(red, "ข้อผิดพลาด: " + green, "URL ต้องเป็น URL ของ YouTube ที่ถูกต้อง")

    else:
        print(red, "ข้อผิดพลาด: กรุณากรอก URL")

except Exception as e:
    print(red, "ข้อผิดพลาด:", green, str(e))
    sys.exit(1)