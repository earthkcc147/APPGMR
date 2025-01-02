import json
import os

def load_emails(file_path):
    """โหลดข้อมูลจากไฟล์ email.json"""
    if not os.path.exists(file_path):
        return {'emails': []}  # ถ้าไฟล์ไม่มี ให้เริ่มต้นใหม่
    with open(file_path, 'r') as file:
        return json.load(file)

def save_emails(file_path, data):
    """บันทึกข้อมูลลงในไฟล์ email.json"""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_email(file_path):
    """เพิ่มอีเมลใหม่"""
    data = load_emails(file_path)
    email = input("กรุณากรอกอีเมลที่ต้องการเพิ่ม: ").strip()
    if email in data['emails']:
        print(f"อีเมล {email} มีอยู่แล้วในรายการ")
    else:
        data['emails'].append(email)
        save_emails(file_path, data)
        print(f"เพิ่มอีเมล {email} สำเร็จ")

def delete_email(file_path):
    """ลบอีเมลออกจากรายการ"""
    data = load_emails(file_path)
    email = input("กรุณากรอกอีเมลที่ต้องการลบ: ").strip()
    if email in data['emails']:
        data['emails'].remove(email)
        save_emails(file_path, data)
        print(f"ลบอีเมล {email} สำเร็จ")
    else:
        print(f"ไม่พบอีเมล {email} ในรายการ")

def display_emails(file_path):
    """แสดงรายการอีเมลทั้งหมด"""
    data = load_emails(file_path)
    if not data['emails']:
        print("ไม่มีอีเมลในรายการ")
    else:
        print("รายการอีเมลทั้งหมด:")
        for index, email in enumerate(data['emails'], start=1):
            print(f"{index}. {email}")

def main():
    file_path = 'function/email/email.json'
    
    while True:
        print("\n--- เมนูการจัดการอีเมล ---")
        print("1. แสดงรายการอีเมล")
        print("2. เพิ่มอีเมล")
        print("3. ลบอีเมล")
        print("4. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1-4): ").strip()
        if choice == '1':
            display_emails(file_path)
        elif choice == '2':
            add_email(file_path)
        elif choice == '3':
            delete_email(file_path)
        elif choice == '4':
            print("ออกจากโปรแกรม")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")

if __name__ == "__main__":
    main()