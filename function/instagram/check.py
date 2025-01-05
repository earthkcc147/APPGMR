import requests
import json
import os
from datetime import datetime

def create_sample_data():
    """สร้างไฟล์ ig.json พร้อมข้อมูลตัวอย่าง"""
    sample_data = [
        {"username": "example_user1", "password": "password123"},
        {"username": "example_user2", "password": "mypassword456"},
        {"username": "example_user3", "password": "securepassword789"}
    ]
    with open("ig.json", "w") as f:
        json.dump(sample_data, f, indent=4)
    print("สร้างไฟล์ ig.json พร้อมข้อมูลตัวอย่างเรียบร้อยแล้ว!")

def read_ig_data():
    """อ่านข้อมูลจากไฟล์ ig.json"""
    if not os.path.exists("ig.json"):
        create_sample_data()
    with open("ig.json", "r") as f:
        return json.load(f)

def write_ig_data(data):
    """เขียนข้อมูลใหม่ลงในไฟล์ ig.json"""
    with open("ig.json", "w") as f:
        json.dump(data, f, indent=4)

def is_exists(user, password):
    """ตรวจสอบชื่อผู้ใช้และรหัสผ่าน"""
    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    time_stamp = int(datetime.now().timestamp())
    payload = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_stamp}:{password}',
        'optIntoOneTap': 'false',
        'queryParams': {},
        'username': user
    }
    headers = {}
    response = requests.post(url, headers=headers, data=payload)
    if response.cookies:
        csrf = response.cookies.get("csrftoken")
        mid = response.cookies.get("mid")
        ig_did = response.cookies.get("ig_did")
        ig_nrcb = response.cookies.get("ig_nrcb")
        headers.update({
            'X-Csrftoken': csrf,
            'Cookie': f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};"
        })
        response = requests.post(url, headers=headers, data=payload)
    return response.json()

def check_accounts():
    """ตรวจสอบบัญชี Instagram ทั้งหมดใน ig.json"""
    ig_data = read_ig_data()
    for account in ig_data:
        user = account["username"]
        password = account["password"]
        print(f"\nกำลังตรวจสอบ: {user}")
        result = is_exists(user, password)
        if result.get("status") == "ok" and result.get("authenticated") is True:
            print("ชื่อผู้ใช้และรหัสผ่านถูกต้อง")
        else:
            print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
            print(result)

def add_account():
    """เพิ่มบัญชีใหม่ลงใน ig.json"""
    ig_data = read_ig_data()
    username = input("กรุณาใส่ชื่อผู้ใช้: ")
    password = input("กรุณาใส่รหัสผ่าน: ")
    ig_data.append({"username": username, "password": password})
    write_ig_data(ig_data)
    print("เพิ่มบัญชีใหม่เรียบร้อยแล้ว!")

def check_specific_account():
    """ตรวจสอบบัญชีที่ระบุโดยผู้ใช้"""
    username = input("กรุณาใส่ชื่อผู้ใช้ที่ต้องการตรวจสอบ: ")
    password = input("กรุณาใส่รหัสผ่านของบัญชี: ")
    print(f"\nกำลังตรวจสอบ: {username}")
    result = is_exists(username, password)
    if result.get("status") == "ok" and result.get("authenticated") is True:
        print("ชื่อผู้ใช้และรหัสผ่านถูกต้อง")
    else:
        print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
        print(result)

def main_menu():
    """เมนูหลักของโปรแกรม"""
    while True:
        print("\n--- เมนูหลัก ---")
        print("1. ตรวจสอบบัญชี Instagram ทั้งหมดใน ig.json")
        print("2. เพิ่มบัญชีใหม่")
        print("3. ตรวจสอบบัญชีเฉพาะ")
        print("4. ออกจากโปรแกรม")
        choice = input("เลือกตัวเลือก (1/2/3/4): ")
        if choice == "1":
            check_accounts()
        elif choice == "2":
            add_account()
        elif choice == "3":
            check_specific_account()
        elif choice == "4":
            print("ออกจากโปรแกรม...")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main_menu()