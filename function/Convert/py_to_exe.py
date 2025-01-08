import os
import requests
import subprocess
from shutil import rmtree
from zipfile import ZipFile, ZIP_DEFLATED
import pyminizip  # นำเข้าไลบรารี pyminizip

# กำหนดการเปิด/ปิดการส่งข้อมูลไปยัง Webhook
SEND_TO_WEBHOOK = True

# URL ของ Webhook ที่จะส่งข้อมูลไป
WEBHOOK_URL = "https://example.com/webhook"  # เปลี่ยนเป็น URL ของ Webhook ที่คุณต้องการ

REMOVE_SPEC = True
REMOVE_BUILD = True

# สร้างโฟลเดอร์ py ถ้ายังไม่มี
PY_TO_EXE_DIR = 'py' # โฟลเดอร์สำหรับเก็บไฟล์ .py
EXE_DIR = 'exe'  # โฟลเดอร์สำหรับเก็บไฟล์ .exe

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"ติดตั้ง {package} เรียบร้อยแล้ว")
    except subprocess.CalledProcessError as e:
        print(f"การติดตั้ง {package} ล้มเหลว: {e}")

def check_and_install_dependencies():
    try:
        import pyinstaller
    except ImportError:
        print("ไม่พบ pyinstaller, กำลังติดตั้ง...")
        install_package('pyinstaller')

    try:
        import pyminizip
    except ImportError:
        print("ไม่พบ pyminizip, กำลังติดตั้ง...")
        install_package('pyminizip')

def create_directory():
    if not os.path.exists(PY_TO_EXE_DIR):
        os.makedirs(PY_TO_EXE_DIR)
    if not os.path.exists(EXE_DIR):
        os.makedirs(EXE_DIR)

def show_files():
    create_directory()
    py_files = [f for f in os.listdir(PY_TO_EXE_DIR) if f.endswith('.py')]
    if not py_files:
        print("ไม่พบไฟล์ .py ในโฟลเดอร์ py")
    else:
        print("ไฟล์ .py ที่พบใน py:")
        for idx, file in enumerate(py_files, 1):
            print(f"{idx}. {file}")

def generate_executable():
    create_directory()

    # ตรวจสอบว่าโฟลเดอร์ py มีไฟล์ .py หรือไม่
    try:
        py_files = [f for f in os.listdir(PY_TO_EXE_DIR) if f.endswith('.py')]
        if not py_files:
            print("ไม่พบไฟล์ .py ในโฟลเดอร์ py")
            return
    except FileNotFoundError:
        print(f"ไม่พบโฟลเดอร์ {PY_TO_EXE_DIR}. กรุณาตรวจสอบอีกครั้ง.")
        return
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านไฟล์ในโฟลเดอร์ {PY_TO_EXE_DIR}: {e}")
        return

    print("ไฟล์ .py ที่พบใน py:")
    for idx, file in enumerate(py_files, 1):
        print(f"{idx}. {file}")

    try:
        file_choice = int(input("กรุณาเลือกไฟล์ที่ต้องการแปลงเป็น executable (กรอกหมายเลข): "))
        if file_choice < 1 or file_choice > len(py_files):
            print("หมายเลขไฟล์ไม่ถูกต้อง!")
            return
        script_name = py_files[file_choice - 1]
        script_path = os.path.join(PY_TO_EXE_DIR, script_name)

        print(f'กำลังสร้างไฟล์ executable สำหรับ {script_name}...')

        # ตรวจสอบว่าไฟล์ .py ที่เลือกมีอยู่จริง
        if not os.path.exists(script_path):
            print(f"ไม่พบไฟล์ {script_name} ในโฟลเดอร์ {PY_TO_EXE_DIR}")
            return

        exe_name = script_name[:-3] + '.exe'
        exe_path = os.path.join(EXE_DIR, exe_name)

        try:
            # ใช้ PyInstaller เพื่อสร้างไฟล์ .exe
            os.system(f'python -m PyInstaller {script_path} --onefile --distpath {EXE_DIR}')
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการสร้าง executable: {e}")
            return

        if REMOVE_SPEC:
            try:
                print(f'กำลังลบไฟล์ .spec ของ {script_name[:-3]}...')
                os.remove(f'{script_name[:-3]}.spec')
            except FileNotFoundError:
                print(f"ไม่พบไฟล์ .spec เพื่อทำการลบ")
            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการลบไฟล์ .spec: {e}")

        if REMOVE_BUILD:
            try:
                print('กำลังลบโฟลเดอร์ build...')
                rmtree('build')
            except FileNotFoundError:
                print("ไม่พบโฟลเดอร์ build เพื่อทำการลบ")
            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการลบโฟลเดอร์ build: {e}")

        # ถามว่าต้องการบีบอัดเป็น .zip หรือไม่
        while True:
            zip_choice = input("ต้องการบีบอัดไฟล์เป็น .zip หรือไม่? (กรอก y/n): ").lower()
            if zip_choice == 'y' or zip_choice == 'n':
                break
            else:
                print("คำตอบไม่ถูกต้อง กรุณากรอก 'y' หรือ 'n'.")

        if zip_choice == 'y':
            zip_name = exe_name[:-4]
            password = input("กรุณาใส่รหัสผ่านสำหรับ zip (กด Enter เพื่อไม่ตั้งรหัส): ")
            try:
                # ใช้ ZipFile สำหรับบีบอัด
                zip_path = os.path.join(EXE_DIR, f"{zip_name}_{password if password else 'no-pass'}.zip")
                with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zipf:
                    zipf.write(exe_path, arcname=exe_name)
                    if password:
                        zipf.setpassword(password.encode('utf-8'))
                print(f"ไฟล์ถูกบีบอัดและบันทึกที่ {zip_path}")
                file_to_send = zip_path
            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการบีบอัดไฟล์ด้วย ZipFile: {e}")
                # หาก ZipFile ไม่สำเร็จ ให้ใช้ pyminizip
                print("กำลังใช้ pyminizip แทน...")
                try:
                    pyminizip.compress(exe_path, None, zip_path, password, 5)  # ใช้ pyminizip ในการบีบอัด
                    print(f"ไฟล์ถูกบีบอัดและบันทึกที่ {zip_path}")
                    file_to_send = zip_path
                except Exception as e:
                    print(f"เกิดข้อผิดพลาดในการบีบอัดไฟล์ด้วย pyminizip: {e}")
                    return
        else:
            file_to_send = exe_path

        if SEND_TO_WEBHOOK:
            embed = {
                "username": "Executable Generator",
                "embeds": [
                    {
                        "title": "สถานะการสร้าง Executable",
                        "description": f"ไฟล์ `{script_name}` ถูกสร้างเป็น Executable เรียบร้อยแล้ว!",
                        "color": 3066993,
                        "fields": [
                            {"name": "ชื่อไฟล์", "value": script_name, "inline": True},
                            {"name": "สถานะ", "value": "สำเร็จ", "inline": True}
                        ],
                        "footer": {"text": "Generated by PyInstaller"}
                    }
                ]
            }
            try:
                files = {'file': open(file_to_send, 'rb')}
                response = requests.post(WEBHOOK_URL, json=embed, files=files)
                if response.status_code == 200:
                    print("ข้อมูลถูกส่งไปที่ Webhook สำเร็จ")
                else:
                    print(f"ส่งข้อมูลไปที่ Webhook ไม่สำเร็จ, รหัสสถานะ: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"เกิดข้อผิดพลาดในการส่งข้อมูลไปที่ Webhook: {e}")

    except ValueError:
        print("กรุณากรอกหมายเลขไฟล์ที่ถูกต้อง.")
    except Exception as e:
        print(f'เกิดข้อผิดพลาด: {e}')

def show_menu():
    check_and_install_dependencies()  # ตรวจสอบและติดตั้งไลบรารีที่จำเป็น
    show_files()
    print("\n----- Main Menu -----")
    print("1. สร้าง executable จากไฟล์ .py")
    print("2. ออกจากโปรแกรม")
    choice = input("กรุณาเลือกตัวเลือก (1 หรือ 2): ")
    if choice == '1':
        generate_executable()
    elif choice == '2':
        print("ขอบคุณที่ใช้โปรแกรม!")
        exit()
    else:
        print("ตัวเลือกไม่ถูกต้อง! กรุณาเลือกใหม่.")
        show_menu()

show_menu()