import os
from glob import glob
from pydub import AudioSegment
import mutagen
from PIL import Image

# กำหนดโฟลเดอร์
input_folder = "convert"
output_folder = os.path.join(input_folder, "finish")

# กำหนดรูปแบบไฟล์ที่รองรับ
SUPPORTED_AUDIO_FORMATS = ['mp3', 'wav', 'flac', 'ogg', 'aac', 'mkv', 'mp4', 'flv', 'aiff', 'opus', 'm4a']
SUPPORTED_IMAGE_FORMATS = ['png', 'jpg', 'jpeg', 'bmp', 'gif']

def setup_directories():
    """ตรวจสอบและสร้างโฟลเดอร์ convert และ convert/finish หากยังไม่มี"""
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"สร้างโฟลเดอร์ {input_folder} เรียบร้อย")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"สร้างโฟลเดอร์ {output_folder} เรียบร้อย")

def show_supported_formats():
    """แสดงรูปแบบไฟล์ที่รองรับการแปลง"""
    print("\n--- รูปแบบไฟล์ที่รองรับการแปลง ---")
    for format in SUPPORTED_AUDIO_FORMATS + SUPPORTED_IMAGE_FORMATS:
        print(f"- {format}")
    print("-------------------------")

def list_files(folder_path, formats):
    """แสดงรายการไฟล์ที่รองรับในโฟลเดอร์"""
    files = glob(os.path.join(folder_path, "*"))
    supported_files = [file for file in files if os.path.splitext(file)[1][1:].lower() in formats]
    
    if not supported_files:
        print("ไม่พบไฟล์ในโฟลเดอร์ที่ระบุ")
        return []

    print("\n--- รายการไฟล์ ---")
    for idx, file in enumerate(supported_files, start=1):
        print(f"{idx}. {os.path.basename(file)}")
    print("-------------------------")
    return supported_files

def audio_conversion():
    """แปลงไฟล์เสียง"""
    songs = list_files(input_folder, SUPPORTED_AUDIO_FORMATS)
    if not songs:
        return

    print("\n--- เลือกไฟล์ที่ต้องการแปลง ---")
    for idx, file in enumerate(songs, start=1):
        print(f"{idx}. {os.path.basename(file)}")
    print("-------------------------")

    selected = input("กรุณาเลือกไฟล์ตามหมายเลข (เช่น 1, 2, 3): ").strip()
    try:
        indices = [int(x) for x in selected.split(",") if x.isdigit()]
        selected_files = [songs[i - 1] for i in indices if 0 < i <= len(songs)]
        if not selected_files:
            print("ไม่มีไฟล์ที่ตรงกับการเลือกของคุณ")
            return
    except Exception:
        print("การเลือกไม่ถูกต้อง")
        return

    output_format = input("กรุณาระบุรูปแบบไฟล์ที่ต้องการแปลง (เช่น wav, mp3): ").strip()
    if output_format not in SUPPORTED_AUDIO_FORMATS:
        print(f"รูปแบบ {output_format} ไม่รองรับ กรุณาลองใหม่")
        return

    for file in selected_files:
        current_format = os.path.splitext(file)[1][1:]  # ดึงนามสกุลไฟล์
        if current_format == output_format:
            print(f"ไม่สามารถแปลงไฟล์ {os.path.basename(file)} เป็น {output_format} เพราะเป็นรูปแบบเดียวกัน")
            continue  # ข้ามไฟล์นี้ไป

        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(file))[0] + f".{output_format}")
        try:
            sound = AudioSegment.from_file(file)
            sound.export(output_file, format=output_format)
            print(f"แปลงไฟล์ {os.path.basename(file)} เป็น {output_format} และเก็บไว้ที่ {output_folder} เรียบร้อย")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการแปลงไฟล์ {os.path.basename(file)}: {e}")

def image_conversion():
    """แปลงไฟล์รูปภาพ"""
    images = list_files(input_folder, SUPPORTED_IMAGE_FORMATS)
    if not images:
        return

    print("\n--- เลือกไฟล์ที่ต้องการแปลง ---")
    for idx, file in enumerate(images, start=1):
        print(f"{idx}. {os.path.basename(file)}")
    print("-------------------------")

    selected = input("กรุณาเลือกไฟล์ตามหมายเลข (เช่น 1, 2, 3): ").strip()
    try:
        indices = [int(x) for x in selected.split(",") if x.isdigit()]
        selected_files = [images[i - 1] for i in indices if 0 < i <= len(images)]
        if not selected_files:
            print("ไม่มีไฟล์ที่ตรงกับการเลือกของคุณ")
            return
    except Exception:
        print("การเลือกไม่ถูกต้อง")
        return

    output_format = input("กรุณาระบุรูปแบบไฟล์ที่ต้องการแปลง (เช่น jpg, png): ").strip()
    if output_format not in SUPPORTED_IMAGE_FORMATS:
        print(f"รูปแบบ {output_format} ไม่รองรับ กรุณาลองใหม่")
        return

    for file in selected_files:
        current_format = os.path.splitext(file)[1][1:].lower()  # ดึงนามสกุลไฟล์
        if current_format == output_format:
            print(f"ไม่สามารถแปลงไฟล์ {os.path.basename(file)} เป็น {output_format} เพราะเป็นรูปแบบเดียวกัน")
            continue  # ข้ามไฟล์นี้ไป

        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(file))[0] + f".{output_format}")
        try:
            img = Image.open(file)
            img.convert("RGB")  # การแปลงภาพเป็น RGB ก่อน
            img.save(output_file, output_format.upper())
            print(f"แปลงไฟล์ {os.path.basename(file)} เป็น {output_format} และเก็บไว้ที่ {output_folder} เรียบร้อย")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการแปลงไฟล์ {os.path.basename(file)}: {e}")

def main_menu():
    """เมนูหลัก"""
    print("\n--- ยินดีต้อนรับเข้าสู่โปรแกรมแปลงไฟล์ ---")
    print("โปรแกรมนี้รองรับการแปลงไฟล์เสียงและรูปภาพหลายรูปแบบ")
    setup_directories()

    while True:
        print("\n--- เมนูหลัก ---")
        print("1. เลือกไฟล์และแปลงไฟล์เสียง")
        print("2. เลือกไฟล์และแปลงไฟล์รูปภาพ")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกตัวเลือก (1/2/3): ").strip()

        if choice == '1':
            audio_conversion()
        elif choice == '2':
            image_conversion()
        elif choice == '3':
            print("ขอบคุณที่ใช้โปรแกรม! ลาก่อน!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main_menu()