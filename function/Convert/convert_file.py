import os
from glob import glob
import pydub
import mutagen

# กำหนดโฟลเดอร์
input_folder = "convert"
output_folder = os.path.join(input_folder, "finish")

# กำหนดรูปแบบไฟล์ที่รองรับ
SUPPORTED_FORMATS = ['mp3', 'wav', 'flac', 'ogg', 'aac', 'mkv', 'mp4', 'flv', 'aiff', 'opus', 'm4a']

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
    for format in SUPPORTED_FORMATS:
        print(f"- {format}")
    print("-------------------------")
    return SUPPORTED_FORMATS

def list_audio_files(folder_path):
    """แสดงรายการไฟล์เสียงในโฟลเดอร์"""
    audio_files = glob(os.path.join(folder_path, "*"))
    if not audio_files:
        print("ไม่พบไฟล์เสียงในโฟลเดอร์ที่ระบุ")
        return []

    print("\n--- รายการไฟล์เสียง ---")
    for idx, file in enumerate(audio_files, start=1):
        print(f"{idx}. {os.path.basename(file)}")
    print("-------------------------")
    return audio_files

def conversion():
    """แปลงไฟล์เสียง"""
    songs = list_audio_files(input_folder)
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
    if output_format not in SUPPORTED_FORMATS:
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
            delete_original = input(f"ต้องการลบไฟล์ต้นฉบับ {os.path.basename(file)} หรือไม่? (y/n): ").strip().lower()
            if delete_original == 'y':
                os.remove(file)
                print("ลบไฟล์ต้นฉบับเรียบร้อย")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการแปลงไฟล์ {os.path.basename(file)}: {e}")

    print("การแปลงไฟล์เสร็จสิ้น")

def show_audio_info():
    """แสดงข้อมูลของไฟล์เสียง"""
    songs = list_audio_files(input_folder)
    if not songs:
        return

    for file in songs:
        try:
            audio_info = mutagen.File(file).info
            print(f"\nข้อมูลไฟล์: {os.path.basename(file)}")
            print(f"   รูปแบบไฟล์: {os.path.splitext(file)[1][1:]}")
            print(f"   อัตราการสุ่มตัวอย่าง: {audio_info.sample_rate} Hz")
            print(f"   ช่องสัญญาณ: {audio_info.channels}")
            print(f"   ระยะเวลา: {audio_info.length:.2f} วินาที")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการอ่านไฟล์ {os.path.basename(file)}: {e}")

def main_menu():
    """เมนูหลัก"""
    print("\n--- ยินดีต้อนรับเข้าสู่โปรแกรมแปลงไฟล์เสียง ---")
    print("โปรแกรมนี้รองรับไฟล์เสียงหลายรูปแบบและช่วยจัดการไฟล์อย่างง่ายดาย")
    setup_directories()
    show_supported_formats()

    while True:
        print("\n--- เมนูหลัก ---")
        print("1. เลือกไฟล์และแปลงไฟล์เสียง")
        print("2. แสดงข้อมูลไฟล์เสียง")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกตัวเลือก (1/2/3): ").strip()

        if choice == '1':
            conversion()
        elif choice == '2':
            print("กำลังแสดงข้อมูลไฟล์เสียง...")
            show_audio_info()
        elif choice == '3':
            print("ขอบคุณที่ใช้โปรแกรม! ลาก่อน!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main_menu()






ต้องการให้สามารถแปลงไฟล์รูปภาพได้เช่น จาก .png เป็น .jpg หรืออื่นๆ โดยใช้ฟังก์ชั่นที่มีอย่าง