import os
from glob import glob
import pydub
import mutagen

def show_supported_formats():
    """แสดงรูปแบบไฟล์ที่รองรับการแปลง"""
    supported_formats = ['mp3', 'wav', 'flac', 'ogg', 'aac', 'mkv', 'mp4', 'flv']
    print("\n--- รูปแบบไฟล์ที่รองรับการแปลง ---")
    for format in supported_formats:
        print(f"- {format}")
    print("-------------------------")
    return supported_formats

def list_audio_files(folder_path):
    """แสดงรายการไฟล์เสียงในโฟลเดอร์"""
    audio_files = glob(folder_path)
    if not audio_files:
        print("ไม่พบไฟล์เสียงในโฟลเดอร์ที่ระบุ")
        return []

    print("\n--- รายการไฟล์เสียง ---")
    for idx, file in enumerate(audio_files, start=1):
        print(f"{idx}. {os.path.basename(file)}")
    print("-------------------------")
    return audio_files

def conversion(song_dir, output_format):
    """แปลงไฟล์เสียง"""
    songs = list_audio_files(song_dir)
    if not songs:
        return

    for file in songs:
        output_file = os.path.splitext(file)[0] + f".{output_format}"
        try:
            sound = pydub.AudioSegment.from_file(file)
            sound.export(output_file, format=output_format)
            print(f"แปลงไฟล์ {os.path.basename(file)} เป็น {output_format} เรียบร้อย")
            delete_original = input(f"ต้องการลบไฟล์ต้นฉบับ {os.path.basename(file)} หรือไม่? (y/n): ").strip().lower()
            if delete_original == 'y':
                os.remove(file)
                print("ลบไฟล์ต้นฉบับเรียบร้อย")
            else:
                print("ไฟล์ต้นฉบับถูกเก็บไว้")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการแปลงไฟล์ {os.path.basename(file)}: {e}")
    print("การแปลงไฟล์เสร็จสิ้น")

def show_audio_info(song_dir):
    """แสดงข้อมูลของไฟล์เสียง"""
    songs = list_audio_files(song_dir)
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
    show_supported_formats()  # แสดงรูปแบบไฟล์ที่รองรับก่อนเมนูหลัก
    while True:
        print("\n--- เมนูหลัก ---")
        print("2. แปลงไฟล์เสียง")
        print("3. แสดงข้อมูลไฟล์เสียง")
        print("4. ออกจากโปรแกรม")
        choice = input("เลือกตัวเลือก (2/3/4): ").strip()

        if choice == '2':
            folder_path = input("กรุณากรอกโฟลเดอร์ที่มีไฟล์เสียง (เช่น /path/to/files/*.mp3 หรือ ./*.mp3): ").strip()
            output_format = input("กรุณาระบุรูปแบบไฟล์ที่ต้องการแปลง (เช่น wav, mp3): ").strip()
            print(f"กำลังแปลงไฟล์จากโฟลเดอร์: {folder_path} เป็นรูปแบบ {output_format}...")
            conversion(folder_path, output_format)
        elif choice == '3':
            folder_path = input("กรุณากรอกโฟลเดอร์ที่มีไฟล์เสียง (เช่น /path/to/files/*.mp3 หรือ ./*.mp3): ").strip()
            print(f"กำลังแสดงข้อมูลไฟล์เสียงจากโฟลเดอร์: {folder_path}")
            show_audio_info(folder_path)
        elif choice == '4':
            print("ขอบคุณที่ใช้โปรแกรม! ลาก่อน!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main_menu()