# เขียนโดย N17RO (noob hackers)

# โมดูลที่ต้องการ
import requests, json
import sys
import os

# สีที่ใช้
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# แบนเนอร์ของสคริปต์
print (red+"""

██╗██████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗███████╗
██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║██████╔╝██║  ██║██████╔╝██║   ██║██╔██╗ ██║█████╗  
██║██╔═══╝ ██║  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══╝  
██║██║     ██████╔╝██║  ██║╚██████╔╝██║ ╚████║███████╗
╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                      v 1.0
"""+red)
print (lgreen+bold+"         <===[[ เขียนโดย N17RO ]]===> \n"+clear)
print (yellow+bold+"   <---(( ค้นหาบน YouTube: Noob Hackers ))--> \n"+clear)

# รับค่า IP address จากผู้ใช้
ip = input("กรุณากรอก IP address ของเป้าหมาย/โฮสต์: ")

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[เหยื่อ]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ผู้ให้บริการอินเทอร์เน็ต]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[องค์กร]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[เมือง]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[ภูมิภาค]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[ลองจิจูด]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[ละติจูด]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[เขตเวลา]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[รหัสไปรษณีย์]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('ยกเลิกการทำงาน, ลาก่อน'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" โปรดตรวจสอบการเชื่อมต่ออินเทอร์เน็ตของคุณ!"+clear)
sys.exit(1)