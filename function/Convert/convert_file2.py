from PIL import Image
import os
from glob import glob

# กำหนดโฟลเดอร์
input_folder = "convert"
output_folder = os.path.join(input_folder, "finish")

# กำหนดรูปแบบไฟล์ที่รองรับ
SUPPORTED_AUDIO_FORMATS = ['mp3', 'wav', 'flac', 'ogg', 'aac', 'mkv', 'mp4', 'flv', 'aiff', 'opus', 'm4a']
SUPPORTED_IMAGE_FORMATS = ['png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff']

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
    for format in SUPPORTED_AUDIO_FORMATS:
        print(f"เสียง: - {format}")
    for format in SUPPORTED_IMAGE_FORMATS:
        print(f"รูปภาพ: - {format}")
    print("-------------------------")
    return SUPPORTED_AUDIO_FORMATS, SUPPORTED_IMAGE_FORMATS

def list_files(folder_path, file_formats):
    """แสดงรายการไฟล์ในโฟลเดอร์ตามรูปแบบที่รองรับ"""
    files = []
    for ext in file_formats:
        files.extend(glob(os.path.join(folder_path, f"*.{ext}")))
    if not files:
        print("ไม่พบไฟล์ในโฟลเดอร์ที่ระบุ")
        return []

    print("\n--- รายการไฟล์ ---")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {os.path.basename(file)}")
    print("-------------------------")
    return files

def conversion_audio():
    """แปลงไฟล์เสียง"""
    songs = list_files(input_folder, SUPPORTED_AUDIO_FORMATS)
    if not songs:
        return

    print("\n--- เลือกไฟล์ที่ต้องการแปลง ---")
    print("0. แปลงไฟล์ทั้งหมด")
    for idx, file in enumerate(songs, start=1):
        print(f"{idx}. {os.path.basename(file)}")
    print("-------------------------")

    selected = input("กรุณาเลือกไฟล์ตามหมายเลข (เช่น 1, 2, 3 หรือ 0 สำหรับทั้งหมด): ").strip()
    if selected == '0':
        selected_files = songs
    else:
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
            sound = pydub.AudioSegment.from_file(file)
            sound.export(output_file, format=output_format)
            print(f"แปลงไฟล์ {os.path.basename(file)} เป็น {output_format} และเก็บไว้ที่ {output_folder} เรียบร้อย")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการแปลงไฟล์ {os.path.basename(file)}: {e}")

def conversion_image():
    """แปลงไฟล์รูปภาพ"""
    images = list_files(input_folder, SUPPORTED_IMAGE_FORMATS)
    if not images:
        return

    print("\n--- เลือกไฟล์ที่ต้องการแปลง ---")
    print("0. แปลงไฟล์ทั้งหมด")
    for idx, file in enumerate(images, start=1):
        print(f"{idx}. {os.path.basename(file)}")
    print("-------------------------")

    selected = input("กรุณาเลือกไฟล์ตามหมายเลข (เช่น 1, 2, 3 หรือ 0 สำหรับทั้งหมด): ").strip()
    if selected == '0':
        selected_files = images
    else:
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
        current_format = os.path.splitext(file)[1][1:]  # ดึงนามสกุลไฟล์
        if current_format == output_format:
            print(f"ไม่สามารถแปลงไฟล์ {os.path.basename(file)} เป็น {output_format} เพราะเป็นรูปแบบเดียวกัน")
            continue  # ข้ามไฟล์นี้ไป

        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(file))[0] + f".{output_format}")
        try:
            image = Image.open(file)
            image.convert('RGB').save(output_file, output_format.upper())
            print(f"แปลงไฟล์ {os.path.basename(file)} เป็น {output_format} และเก็บไว้ที่ {output_folder} เรียบร้อย")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการแปลงไฟล์ {os.path.basename(file)}: {e}")

def main_menu():
    """เมนูหลัก"""
    print("\n--- ยินดีต้อนรับเข้าสู่โปรแกรมแปลงไฟล์ ---")
    print("โปรแกรมนี้รองรับไฟล์เสียงหลายรูปแบบและช่วยจัดการไฟล์อย่างง่ายดาย")
    setup_directories()
    show_supported_formats()

    while True:
        print("\n--- เมนูหลัก ---")
        print("1. แปลงไฟล์เสียง")
        print("2. แปลงไฟล์รูปภาพ")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกตัวเลือก (1/2/3): ").strip()

        if choice == '1':
            conversion_audio()
        elif choice == '2':
            conversion_image()
        elif choice == '3':
            print("ขอบคุณที่ใช้โปรแกรม! ลาก่อน!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main_menu()