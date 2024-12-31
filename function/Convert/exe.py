import os
import shutil
import requests

# ตรวจสอบว่ามีการติดตั้ง PyInstaller หรือไม่
try:
    import PyInstaller
except ImportError:
    print("PyInstaller ยังไม่ได้ติดตั้ง กรุณาติดตั้งโดยใช้คำสั่ง: pip install pyinstaller")
    exit()

def send_to_discord(file_path, webhook_url):
    # ตรวจสอบว่าไฟล์มีอยู่จริง
    if not os.path.exists(file_path):
        print(f"ไม่พบไฟล์ที่ต้องการส่ง: {file_path}")
        return

    # ส่งไฟล์ไปยัง Discord ผ่าน Webhook
    with open(file_path, 'rb') as file:
        response = requests.post(
            webhook_url,
            files={'file': file},
            data={'content': 'ไฟล์ EXE ที่แปลงแล้ว'}
        )
    
    if response.status_code == 200:
        print("ไฟล์ถูกส่งไปยัง Discord สำเร็จ")
    else:
        print(f"เกิดข้อผิดพลาดในการส่งไฟล์ไปยัง Discord: {response.status_code} - {response.text}")

def convert_to_exe(script_path, webhook_url):
    # ตรวจสอบว่าไฟล์ที่ระบุเป็นไฟล์ .py
    if not script_path.endswith('.py'):
        print("กรุณาระบุไฟล์ .py ที่ถูกต้อง")
        return

    # ตรวจสอบว่าไฟล์ที่ระบุมีอยู่จริง
    if not os.path.exists(script_path):
        print(f"ไฟล์ {script_path} ไม่พบ")
        return

    # เลือกตัวเลือกคอนโซล
    console_option = input("ต้องการแสดงคอนโซลหรือไม่? (yes/no): ").strip().lower()
    if console_option == 'no':
        command = f"pyinstaller --onefile --noconsole {script_path}"
    else:
        command = f"pyinstaller --onefile {script_path}"

    # ใช้ os.system เพื่อเรียกคำสั่ง
    result = os.system(command)
    if result != 0:
        print("เกิดข้อผิดพลาดระหว่างการแปลงไฟล์ ตรวจสอบว่า PyInstaller ทำงานได้ถูกต้อง")
        return

    # เช็คผลลัพธ์หลังจากคำสั่งเสร็จสิ้น
    exe_filename = os.path.basename(script_path).replace('.py', '.exe')
    exe_path = f"dist/{exe_filename}"

    if os.path.exists(exe_path):
        print(f"ไฟล์ EXE ถูกสร้างสำเร็จ: {exe_path}")

        # ส่งไฟล์ไปยัง Discord
        send_to_discord(exe_path, webhook_url)
    else:
        print("เกิดข้อผิดพลาดในการสร้างไฟล์ EXE")

    # ลบไฟล์ชั่วคราว
    spec_file = script_path.replace('.py', '.spec')
    temp_dirs = ['build', spec_file]
    for item in temp_dirs:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.rmtree(item)  # ลบโฟลเดอร์
            else:
                os.remove(item)  # ลบไฟล์

if __name__ == "__main__":
    print("=== โปรแกรมแปลงไฟล์ .py เป็น .exe ===")
    print("กรุณาระบุชื่อไฟล์ .py ที่ต้องการแปลง")
    print("ไฟล์ .exe จะถูกสร้างในโฟลเดอร์ 'dist/'")
    script_file = input("กรุณาระบุชื่อไฟล์ .py: ")
    
    # URL ของ Discord Webhook
    webhook_url = input("กรุณาระบุ URL ของ Discord Webhook: ")

    # เรียกฟังก์ชันแปลงไฟล์และส่งไปยัง Discord
    convert_to_exe(script_file, webhook_url)