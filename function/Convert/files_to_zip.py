import os
from zipfile import ZipFile, ZIP_DEFLATED

def zip_files_from_folder(folder_path):
    try:
        # ตรวจสอบว่าโฟลเดอร์มีอยู่จริง
        if not os.path.exists(folder_path):
            print(f"ไม่พบโฟลเดอร์ {folder_path}. กรุณาตรวจสอบอีกครั้ง.")
            return
        
        # ใช้ชื่อของโฟลเดอร์เป็นชื่อไฟล์ .zip
        folder_name = os.path.basename(folder_path)
        output_zip_path = f"{folder_name}.zip"
        
        # สร้างไฟล์ zip ใหม่
        with ZipFile(output_zip_path, 'w', ZIP_DEFLATED) as zipf:
            # วนลูปไฟล์ทั้งหมดในโฟลเดอร์
            for folder_name, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    # สร้าง path ของไฟล์
                    file_path = os.path.join(folder_name, filename)
                    # เพิ่มไฟล์ไปยังไฟล์ .zip
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
        
        print(f"ไฟล์ถูกบีบอัดสำเร็จและบันทึกที่ {output_zip_path}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# รับ input โฟลเดอร์จากผู้ใช้
folder_to_zip = input("กรุณากรอกชื่อโฟลเดอร์ที่ต้องการบีบอัด: ")

# ตรวจสอบว่าโฟลเดอร์อยู่ในตำแหน่งเดียวกับไฟล์หลัก
current_directory = os.path.dirname(os.path.realpath(__file__))  # หาตำแหน่งไฟล์หลัก
folder_path = os.path.join(current_directory, folder_to_zip)

# เรียกใช้ฟังก์ชันการบีบอัดไฟล์
zip_files_from_folder(folder_path)