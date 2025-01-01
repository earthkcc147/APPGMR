from tqdm import tqdm
import time
import random  # ใช้สำหรับการสุ่มค่า

# กำหนดค่าที่สามารถปรับได้
total_size_in_mb = 183  # ขนาดไฟล์ (MB)
min_chunk_size_mb = 0.5  # ขนาดไฟล์ขั้นต่ำที่ดาวน์โหลดในแต่ละรอบ (MB)
max_chunk_size_mb = 2    # ขนาดไฟล์สูงสุดที่ดาวน์โหลดในแต่ละรอบ (MB)
min_sleep_time = 0.05    # เวลาหยุดจำลอง (วินาที) สำหรับการดาวน์โหลดที่เร็ว
max_sleep_time = 0.2     # เวลาหยุดจำลอง (วินาที) สำหรับการดาวน์โหลดที่ช้า

def simulate_download():
    # แปลงขนาดไฟล์จาก MB เป็น bytes
    total_size_in_bytes = total_size_in_mb * 1024 * 1024  # ขนาดไฟล์ทั้งหมดใน bytes
    
    # สร้าง progress bar ด้วย tqdm
    with tqdm(total=total_size_in_bytes, unit='B', unit_scale=True, desc="Starting program download") as bar:
        # จำลองการดาวน์โหลดโดยการเพิ่มค่าลงใน progress bar
        downloaded = 0
        while downloaded < total_size_in_bytes:
            # สุ่มขนาดไฟล์ที่ดาวน์โหลดในแต่ละรอบ
            chunk_size_mb = random.uniform(min_chunk_size_mb, max_chunk_size_mb)  # สุ่มขนาดระหว่าง min และ max
            chunk_size_bytes = chunk_size_mb * 1024 * 1024  # แปลงเป็น bytes
            
            # สุ่มเวลาหยุดการดาวน์โหลด
            sleep_time = random.uniform(min_sleep_time, max_sleep_time)  # สุ่มเวลาในช่วงที่กำหนด
            
            # จำลองการดาวน์โหลด (เพิ่มขนาดไฟล์ที่ดาวน์โหลดในแต่ละรอบ)
            time.sleep(sleep_time)  # แสดงการจำลองให้ช้าลงเล็กน้อย
            downloaded += chunk_size_bytes  # เพิ่มขนาดไฟล์ที่ดาวน์โหลดในแต่ละรอบ
            bar.update(chunk_size_bytes)  # อัพเดต progress bar
            
    print(f"ดาวน์โหลดเสร็จสิ้น")

# เรียกใช้ฟังก์ชัน
simulate_download()



ทำไมหลอดดาวโหลดขนาดความกว้างมันเล็กจัง