import subprocess
import sys

# กำหนดโมดูลที่ต้องการติดตั้งในตัวแปร modules
modules = ['selenium', 'pyperclip', 'mechanize', 'beautifulsoup4']

# ฟังก์ชันติดตั้งโมดูล
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# ตรวจสอบและติดตั้งโมดูล
for module in modules:
    try:
        __import__(module)  # ลอง import โมดูล
        print(f"{module} โมดูลถูกติดตั้งแล้ว.")
    except ImportError:
        print(f"กำลังติดตั้ง {module}...")
        install_package(module)

print("การติดตั้งเสร็จสมบูรณ์.")