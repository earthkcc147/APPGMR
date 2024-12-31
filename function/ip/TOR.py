import os, sys, time

# รับค่าจากผู้ใช้เป็นเวลาระหว่างการเปลี่ยนโหนด TOR (ในวินาที)
timetonodechange = int(input("กรุณาใส่เวลาระหว่างการเปลี่ยนโหนด TOR (เป็นวินาที): "))
os.system("clear")

# เริ่มต้น anonsurf
os.system("anonsurf start") 
time.sleep(2.5)
os.system("anonsurf status")
time.sleep(2.5)
os.system("anonsurf myip")
time.sleep(2.5)
os.system("clear")

# ตัวแปรสำหรับการวนลูป
i = 0

# ฟังก์ชันสำหรับการเปลี่ยน IP
def ipchange():
   os.system("anonsurf myip")
   time.sleep(2.5)  
   os.system("anonsurf change")
   time.sleep(2.5)  
   os.system("anonsurf myip") 
   time.sleep(2.5)  
   os.system("clear") 

# วนลูปเพื่อเปลี่ยน IP ตามเวลาที่กำหนด
while i == 0:
   time.sleep(timetonodechange)
   ipchange()