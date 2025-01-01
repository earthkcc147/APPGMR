pip install pillow numpy


from PIL import Image
import numpy as np
import os

# กำหนดตัวอักษรที่ใช้แทนความมืดในภาพ
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# ฟังก์ชันแปลงภาพเป็นขาวดำ
def grayscale_image(image_path):
    try:
        # เปิดภาพ
        image = Image.open(image_path)
        # แปลงเป็นขาวดำ
        grayscale_image = image.convert("L")
        return grayscale_image
    except Exception as e:
        print(f"ไม่สามารถเปิดหรือแปลงภาพได้: {e}")
        return None

# ฟังก์ชันแปลงภาพเป็นข้อความ ASCII
def image_to_ascii(image, new_width=100):
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width)
    # ปรับขนาดภาพใหม่
    image = image.resize((new_width, new_height))
    # แปลงภาพเป็น numpy array
    pixels = np.array(image)
    # สร้างข้อความ ASCII
    ascii_str = ""
    for pixel in pixels:
        for value in pixel:
            ascii_str += ASCII_CHARS[value // 25]  # แบ่งค่าพิกเซลออกเป็นช่วง
        ascii_str += "\n"
    return ascii_str

# ฟังก์ชันหลักในการรับไฟล์ภาพและแสดงผลลัพธ์
def main():
    # รับชื่อไฟล์จาก input
    image_name = input("กรุณากรอกชื่อไฟล์ภาพ (เช่น image.jpg): ")
    
    # ตรวจสอบว่าไฟล์นั้นมีอยู่ในโฟลเดอร์เดียวกับโปรเจคหรือไม่
    if not os.path.isfile(image_name):
        print("ไม่พบไฟล์ที่ระบุในโฟลเดอร์ปัจจุบัน")
        return
    
    # แปลงภาพเป็นขาวดำ
    grayscale_img = grayscale_image(image_name)
    if grayscale_img:
        # แปลงภาพเป็นข้อความ ASCII
        ascii_result = image_to_ascii(grayscale_img)
        # แสดงผล
        print(ascii_result)

if __name__ == "__main__":
    main()





เพิ่มให้บันทึกข้อความไว้ที่ (ชื่อไฟล์).json โดยการสร้างอัตโนมัติ