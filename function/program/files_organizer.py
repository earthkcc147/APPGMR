import os
import glob

# ใช้ฟังก์ชัน glob ของโมดูล glob เพื่อหาทุกไฟล์ในโฟลเดอร์ปัจจุบัน
files_list = glob.glob("*")
# สร้างเซ็ตของประเภทนามสกุลไฟล์ในโฟลเดอร์เพื่อหลีกเลี่ยงการเพิ่มรายการซ้ำ
extension_set = set()
# เพิ่มประเภทนามสกุลแต่ละตัวเข้าไปในเซ็ต
for file in files_list:
    extension = file.split(sep=".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue

# ฟังก์ชันสร้างโฟลเดอร์สำหรับแต่ละประเภทนามสกุล
def createDirs():
    for dir in extension_set:
        folder_name = dir + "_files"
        if os.path.exists(folder_name):
            print(f"⚠️ โฟลเดอร์ '{folder_name}' มีอยู่แล้ว!")
        else:
            try:
                os.makedirs(folder_name)
                print(f"✅ สร้างโฟลเดอร์ '{folder_name}' เรียบร้อยแล้ว!")
            except Exception as e:
                print(f"❌ เกิดข้อผิดพลาดในการสร้างโฟลเดอร์ '{folder_name}': {e}")
        print("="*40)  # ขีดคั่นระหว่างการสร้างโฟลเดอร์

# ฟังก์ชันย้ายไฟล์ไปยังโฟลเดอร์ที่เหมาะสม
def arrange():
    for file in files_list:
        fextension = file.split(sep=".")
        try:
            destination = fextension[1] + "_files/" + file
            if not os.path.exists(destination):
                os.rename(file, destination)
                print(f"✅ ย้ายไฟล์ '{file}' ไปยัง '{destination}' เรียบร้อยแล้ว!")
            else:
                print(f"⚠️ ไฟล์ '{file}' มีอยู่แล้วในโฟลเดอร์ '{fextension[1]}_files'")
        except (OSError, IndexError) as e:
            print(f"❌ เกิดข้อผิดพลาดในการย้ายไฟล์ '{file}': {e}")
        print("="*40)  # ขีดคั่นระหว่างการย้ายไฟล์

# ฟังก์ชันสำหรับแสดงวิธีการใช้งาน
def showInstructions():
    print("\n" + "="*40)
    print("🎉 --- วิธีการใช้งาน --- 🎉")
    print("โปรแกรมนี้ใช้สำหรับการจัดระเบียบไฟล์ในโฟลเดอร์ปัจจุบัน")
    print("โดยการจัดไฟล์ตามประเภทนามสกุลของไฟล์ เช่น .txt, .jpg, .pdf เป็นต้น")
    print("เมื่อเลือกตัวเลือก 'จัดระเบียบไฟล์' โปรแกรมจะสร้างโฟลเดอร์ที่แยกตามนามสกุลไฟล์")
    print("และย้ายไฟล์ไปไว้ในโฟลเดอร์ที่เหมาะสม\n")
    print("🚨 หากต้องการออกจากโปรแกรม ให้เลือกตัวเลือก 'ออกจากโปรแกรม' 🚨")
    print("="*40)

# ฟังก์ชันสำหรับเมนูหลัก
def mainMenu():
    while True:
        print("\n" + "="*40)
        print("📝 --- เมนูหลัก --- 📝")
        print("1. จัดระเบียบไฟล์")
        print("2. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1/2): ")

        if choice == '1':
            createDirs()
            arrange()
            print("\n✅ ไฟล์ถูกจัดระเบียบเรียบร้อยแล้ว!")
            print("="*40)  # ขีดคั่นหลังจากการจัดระเบียบไฟล์
        elif choice == '2':
            print("\n🚪 ออกจากโปรแกรม...")
            break
        else:
            print("\n⚠️ กรุณาเลือกตัวเลือกที่ถูกต้อง!")
            print("="*40)  # ขีดคั่นกรณีเลือกตัวเลือกที่ไม่ถูกต้อง

# เรียกใช้ฟังก์ชันแสดงวิธีการใช้งานก่อนเมนูหลัก
showInstructions()

# เรียกใช้เมนูหลัก
mainMenu()