from pytube import YouTube
import os

# กำหนดโฟลเดอร์สำหรับบันทึกไฟล์
save_path = os.path.join(os.getcwd(), 'VDO')  # กำหนดโฟลเดอร์ VDO ที่ตำแหน่งเดียวกันกับ main.py

# ตรวจสอบว่ามีโฟลเดอร์สำหรับบันทึกไฟล์อยู่หรือไม่ หากไม่มีให้สร้างขึ้นมา
if not os.path.exists(save_path):
    os.makedirs(save_path)

# กำหนดที่อยู่ของไฟล์ links.txt
link_file = os.path.join(os.getcwd(), 'links.txt')

# ตรวจสอบว่าไฟล์ links.txt มีอยู่หรือไม่ หากไม่มีก็จะสร้างขึ้นมา
if not os.path.exists(link_file):
    with open(link_file, 'w') as file:
        # ตัวอย่างลิงก์ที่ต้องการให้ในไฟล์ links.txt
        file.write("https://www.youtube.com/watch?v=I28wvv_6z0s\n")
        file.write("https://www.youtube.com/watch?v=TVcH4vnYK8g\n")
        file.write("https://www.youtube.com/watch?v=tbYpXJcc6NE\n")
    print(f"ไฟล์ {link_file} ถูกสร้างขึ้นมาใหม่.")

# อ่านลิงก์จากไฟล์
with open(link_file, 'r') as link:
    # ตัวนับจำนวนลิงก์ที่ดาวน์โหลด
    count = 0

    for i in link:
        try:
            # ดึงรายละเอียดวิดีโอ YouTube จากลิงก์
            x = YouTube(i.strip())  # ใช้ .strip() เพื่อลบช่องว่างหรือ newline

            print('เริ่มดาวน์โหลด: ' + x.title)
            # เลือกดาวน์โหลดแบบ progressive (วิดีโอและเสียงรวมกัน)
            x.streams.filter(progressive="true")

            # ดาวน์โหลดคุณภาพวิดีโอที่มีอยู่ตัวแรก
            x.streams.first().download(save_path)

            print('ดาวน์โหลดเสร็จสิ้น: ' + x.title)
            print('-------------------------------------' + "\n")

            # เพิ่มจำนวนตัวนับเมื่อดาวน์โหลดสำเร็จ
            count += 1

        except Exception as e:
            print(f"เกิดข้อผิดพลาดในลิงก์นี้: {i.strip()} | ข้อผิดพลาด: {e}")

    # แสดงผลรวม
    print('ลิงก์ทั้งหมดถูกประมวลผล')
    print('จำนวนลิงก์ที่ดาวน์โหลดสำเร็จ: ' + str(count))