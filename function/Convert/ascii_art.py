import pyfiglet
import os

# ฟังก์ชันหลัก
def main():
    # รับข้อความจากผู้ใช้
    text = input("กรุณาใส่ข้อความที่ต้องการแปลง: ")
    if not text.strip():
        print("กรุณาใส่ข้อความที่ถูกต้อง")
        return

    # ดึงรายชื่อฟอนต์ทั้งหมด
    fonts = pyfiglet.FigletFont.getFonts()

    # สร้างชื่อไฟล์ .txt
    filename = f"{text}.txt"
    filename = filename.replace(" ", "_")  # แทนที่ช่องว่างในชื่อไฟล์ด้วย "_"

    # สร้างไฟล์และเขียนผลลัพธ์
    with open(filename, "w", encoding="utf-8") as f:
        for font in fonts:
            try:
                # แปลงข้อความเป็น ASCII Art ด้วยฟอนต์นั้น ๆ
                ascii_art = pyfiglet.figlet_format(text, font=font)
                f.write(f"ฟอนต์: {font}\n")
                f.write(ascii_art)
                f.write("\n" + "-"*80 + "\n")  # เส้นคั่นระหว่างฟอนต์
            except pyfiglet.FontNotFound:
                # หากเกิดข้อผิดพลาดในการใช้ฟอนต์ ให้ข้ามไป
                print(f"ฟอนต์ '{font}' ไม่สามารถใช้งานได้")

    print(f"บันทึกผลลัพธ์ในไฟล์ '{filename}' สำเร็จ")

# เรียกใช้งานฟังก์ชันหลัก
if __name__ == "__main__":
    main()