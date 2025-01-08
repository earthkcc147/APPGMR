from PIL import Image
import io
import os

SOURCE_DIR = 'source'  # โฟลเดอร์ที่เก็บไฟล์สคริปต์
IMG_DIR = 'img'  # โฟลเดอร์ที่เก็บไฟล์ภาพ
SRCIMG_DIR = 'srcimg'  # โฟลเดอร์ที่เก็บไฟล์ภาพที่เพิ่มสคริปต์เข้าไป

def list_files(directory):
    """ฟังก์ชันสำหรับแสดงชื่อไฟล์ในโฟลเดอร์"""
    try:
        files = os.listdir(directory)
        if not files:
            print("ไม่มีไฟล์ในโฟลเดอร์นี้.")
        else:
            print(f"ไฟล์ในโฟลเดอร์ {directory}:")
            for file in files:
                print(file)
    except FileNotFoundError:
        print(f"ไม่พบโฟลเดอร์ {directory}")

def embed_script(image_name, script_name, output_name):
    # สร้าง path สำหรับไฟล์ที่ต้องการ
    image_path = os.path.join(IMG_DIR, image_name)
    script_path = os.path.join(SOURCE_DIR, script_name)
    output_path = os.path.join(SRCIMG_DIR, output_name)

    # เปิดไฟล์ภาพต้นฉบับ
    img = Image.open(image_path)
    
    # อ่านไฟล์สคริปต์
    with open(script_path, 'r', encoding='utf-8') as script_file:
        script = script_file.read()
    
    # แปลงสคริปต์เป็นไบต์
    script_bytes = script.encode('utf-8')

    # อ่านข้อมูลภาพต้นฉบับ
    img_bytes = io.BytesIO()
    img.save(img_bytes, format=img.format)  # บันทึกภาพไปยังบัฟเฟอร์ไบต์ ใช้ format ของภาพต้นฉบับ
    img_data = img_bytes.getvalue()

    # เพิ่มสคริปต์เข้าไปในข้อมูลภาพ
    new_data = img_data + script_bytes

    # เขียนข้อมูลใหม่ลงในไฟล์ภาพใหม่
    with open(output_path, 'wb') as f:
        f.write(new_data)

    print(f"สคริปต์ถูกเพิ่มในไฟล์ภาพและบันทึกที่ {output_path}")

def extract_script(image_name):
    # สร้าง path สำหรับไฟล์ที่ต้องการ
    image_path = os.path.join(SRCIMG_DIR, image_name)

    # อ่านข้อมูลจากไฟล์ภาพ
    with open(image_path, 'rb') as f:
        img_data = f.read()

    # ค้นหาตำแหน่งของข้อมูลสคริปต์ (ข้อมูลหลังจากข้อมูลภาพ)
    script_start_index = len(img_data) - img_data[::-1].find(b'\x89PNG\r\n\x1a\n') - 8  # ค้นหาตำแหน่งที่เริ่มต้นของสคริปต์
    script_bytes = img_data[script_start_index:]  # ดึงข้อมูลหลังจากนั้นทั้งหมด
    script = script_bytes.decode('utf-8')

    return script

def show_help():
    """ฟังก์ชันที่แสดงวิธีการใช้งานโปรแกรม"""
    print("\n===== วิธีใช้งานโปรแกรม =====")
    print("1. โปรแกรมนี้สามารถเพิ่มสคริปต์เข้าไปในไฟล์ภาพ PNG หรือ JPG และบันทึกภาพใหม่พร้อมกับสคริปต์ที่ฝังอยู่")
    print("2. เมื่อเลือกเพิ่มสคริปต์ในภาพ โปรแกรมจะขอให้เลือกไฟล์ภาพจากโฟลเดอร์ 'img' และเลือกไฟล์สคริปต์จากโฟลเดอร์ 'source'")
    print("3. โปรแกรมจะเพิ่มเนื้อหาของสคริปต์เข้าไปในไฟล์ภาพและบันทึกเป็นไฟล์ใหม่ในโฟลเดอร์ 'srcimg'")
    print("4. หากต้องการดึงสคริปต์จากไฟล์ภาพที่เพิ่มสคริปต์ไว้แล้ว สามารถเลือกตัวเลือกดึงสคริปต์จากภาพ")
    print("5. โปรแกรมจะค้นหาสคริปต์จากไฟล์ภาพในโฟลเดอร์ 'srcimg' และแสดงผลลัพธ์ให้ผู้ใช้เห็น")
    print("\n===== หมายเหตุ =====")
    print(" - ชื่อไฟล์ในแต่ละโฟลเดอร์จะต้องตรงกันกับไฟล์ที่ต้องการใช้งาน")
    print(" - ต้องตรวจสอบว่าโฟลเดอร์และไฟล์มีอยู่จริงก่อนใช้งาน")

def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. เพิ่มสคริปต์เข้าไปในภาพ")
        print("2. ดึงสคริปต์จากภาพ")
        print("3. ดูวิธีใช้งาน")
        print("4. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1/2/3/4): ")
        
        if choice == '1':
            # แสดงชื่อไฟล์ในโฟลเดอร์ img และ source
            list_files(IMG_DIR)
            list_files(SOURCE_DIR)
            
            # เพิ่มสคริปต์เข้าไปในภาพ
            image_name = input("กรุณาใส่ชื่อไฟล์ภาพ (ในโฟลเดอร์ img): ")
            script_name = input("กรุณาใส่ชื่อไฟล์สคริปต์ (ในโฟลเดอร์ source): ")
            output_name = input("กรุณาใส่ชื่อไฟล์ภาพที่ต้องการบันทึก (ในโฟลเดอร์ srcimg): ")
            embed_script(image_name, script_name, output_name)
        elif choice == '2':
            # แสดงชื่อไฟล์ในโฟลเดอร์ srcimg
            list_files(SRCIMG_DIR)

            # ดึงสคริปต์จากภาพ
            image_name = input("กรุณาใส่ชื่อไฟล์ภาพ (ในโฟลเดอร์ srcimg): ")
            extracted_script = extract_script(image_name)
            print("สคริปต์ที่ดึงออกมา:", extracted_script)
        elif choice == '3':
            # แสดงวิธีใช้งาน
            show_help()
        elif choice == '4':
            # ออกจากโปรแกรม
            print("ขอบคุณที่ใช้งาน!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง.")

if __name__ == '__main__':
    main_menu()