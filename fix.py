import subprocess
import sys

# กำหนดโมดูลที่ต้องการติดตั้งในตัวแปร modules
modules = ['selenium', 'pyperclip', 'mechanize', 'beautifulsoup4', 'pyinstaller', 'pytube', 'colorama']

# ฟังก์ชันติดตั้งโมดูล
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} ติดตั้งสำเร็จ.")
    except Exception as e:
        print(f"ไม่สามารถติดตั้ง {package} ได้: {e}")

# ตรวจสอบและติดตั้งโมดูล
for module in modules:
    try:
        __import__(module)  # ลอง import โมดูล
        print(f"{module} โมดูลถูกติดตั้งแล้ว.")
    except ImportError:
        print(f"กำลังติดตั้ง {module}...")
        install_package(module)

print("การติดตั้งเสร็จสมบูรณ์.")