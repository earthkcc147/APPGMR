import requests
import magic

# รับ file_id และชื่อไฟล์จากผู้ใช้
file_id = input("กรุณากรอก file_id ของไฟล์: ")
file_name_input = input("กรุณากรอกชื่อไฟล์ (ไม่ต้องใส่นามสกุล): ")

# URL ของไฟล์ใน Google Drive
url = f'https://drive.google.com/uc?id={file_id}'

# ส่งคำขอไปยัง URL
response = requests.get(url, stream=True)

# ตรวจสอบประเภทของไฟล์
file_type = magic.from_buffer(response.content, mime=True)

# แสดงประเภทไฟล์
print("ประเภทไฟล์:", file_type)

# ตั้งนามสกุลไฟล์ให้เหมาะสม
if 'pdf' in file_type:
    file_extension = '.pdf'
elif 'zip' in file_type:
    file_extension = '.zip'
elif 'rar' in file_type:
    file_extension = '.rar'
elif 'msword' in file_type:
    file_extension = '.doc'
elif 'vnd.openxmlformats-officedocument.wordprocessingml.document' in file_type:
    file_extension = '.docx'
elif 'mp4' in file_type:
    file_extension = '.mp4'
elif 'mp3' in file_type:
    file_extension = '.mp3'
elif 'png' in file_type:
    file_extension = '.png'
elif 'jpeg' in file_type or 'jpg' in file_type:
    file_extension = '.jpg'  # รองรับทั้ง .jpg และ .jpeg
else:
    file_extension = '.bin'  # ถ้าไม่สามารถตรวจสอบประเภทได้

# ตั้งชื่อไฟล์ที่รับจากผู้ใช้ และเพิ่มนามสกุลไฟล์
file_name = f"{file_name_input}{file_extension}"

# เขียนไฟล์ลงในเครื่อง
with open(file_name, 'wb') as f:
    f.write(response.content)

print(f"ดาวน์โหลดไฟล์สำเร็จ: {file_name}")