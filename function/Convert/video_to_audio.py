__author__ = "Sri Manikanta Palakollu"
__date__ = "01-07-2020"

import moviepy.editor as editor
import os

# การรับข้อมูลจากผู้ใช้ผ่าน input (รับแค่ชื่อไฟล์ ไม่รับพาธ)
videoFile = input("กรุณาใส่ชื่อไฟล์วิดีโอ: ")
audioFileName = input("กรุณาใส่ชื่อไฟล์เสียงที่ต้องการบันทึก (เช่น output_audio.mp3): ")

# หาตำแหน่งที่ไฟล์ Python สคริปต์อยู่
current_dir = os.path.dirname(os.path.realpath(__file__))

# สร้างพาธเต็มสำหรับไฟล์วิดีโอและไฟล์เสียงที่จะบันทึกในตำแหน่งเดียวกัน
videoFilePath = os.path.join(current_dir, videoFile)
audioFilePath = os.path.join(current_dir, audioFileName)

# ตรวจสอบว่ามีไฟล์วิดีโอที่ระบุหรือไม่
if not os.path.exists(videoFilePath):
    print(f"ไม่พบไฟล์วิดีโอที่ตำแหน่ง: {videoFilePath}")
else:
    try:
        # เปิดไฟล์วิดีโอจากตำแหน่งที่ไฟล์สคริปต์อยู่
        videoClip = editor.VideoFileClip(videoFilePath)
        # แปลงเสียงจากวิดีโอและบันทึกเป็นไฟล์เสียงในตำแหน่งเดียวกัน
        videoClip.audio.write_audiofile(audioFilePath)
        print("การแปลงไฟล์เสร็จสมบูรณ์แล้ว!")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดระหว่างการแปลงไฟล์วิดีโอเป็นไฟล์เสียง: {e}")

# ตรวจสอบว่าไฟล์เสียงถูกบันทึกสำเร็จหรือไม่
if os.path.exists(audioFilePath):
    print(f"ไฟล์เสียงถูกบันทึกที่ตำแหน่ง: {audioFilePath}")
else:
    print(f"ไม่สามารถบันทึกไฟล์เสียงที่ตำแหน่ง: {audioFilePath}")