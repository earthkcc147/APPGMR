import os, shutil, sys, instaloader
from prettytable import PrettyTable

# สร้างตัวอินสแตนซ์ของ Instaloader
instagramBot = instaloader.Instaloader(quiet=True)

# ฟังก์ชันสำหรับการเข้าสู่ระบบ
def auth():
    # ป้อนชื่อผู้ใช้ Instagram
    userName = input("กรุณาป้อนชื่อผู้ใช้ Instagram ของคุณ: ")
    try:
        # พยายามโหลดข้อมูลการเข้าสู่ระบบจากไฟล์ที่บันทึกไว้
        instagramBot.load_session_from_file(userName)
    except:
        try:
            # สร้างข้อมูลการเข้าสู่ระบบใหม่
            os.system("instaloader -l {0}".format(userName))
            instagramBot.load_session_from_file(userName)
        except:
            # ทำการเข้าสู่ระบบ
            instagramBot.login(userName, input("กรุณาป้อนรหัสผ่าน: "))
            instagramBot.save_session_to_file()
    print("{0} เข้าสู่ระบบเรียบร้อย.".format(userName))

# ฟังก์ชันดาวน์โหลดข้อมูลทั้งหมดของผู้ใช้
def download_user_data():
    username = input("กรุณาป้อนชื่อผู้ใช้ที่ต้องการดาวน์โหลดข้อมูล: ")
    try:
        profile = instaloader.Profile.from_username(instagramBot.context, username)
    except:
        print("ไม่พบชื่อผู้ใช้นี้.")
        return
    
    currentPath = os.getcwd()
    user_folder = os.path.join(currentPath, username)  # สร้างโฟลเดอร์ผู้ใช้
    if not os.path.exists(user_folder):
        os.mkdir(user_folder)
    
    # ดาวน์โหลดโปรไฟล์ข้อมูล (เช่น ชื่อผู้ใช้, ชื่อเต็ม, จำนวนโพสต์)
    profile_info = {
        "Username": profile.username,
        "Full Name": profile.full_name,
        "Bio": profile.biography,
        "Followers": profile.followers,
        "Following": profile.followees,
        "Posts": profile.mediacount,
        "Profile Pic": profile.profile_pic_url
    }
    
    print("ข้อมูลของผู้ใช้ {0}:\n".format(username))
    for key, value in profile_info.items():
        print(f"{key}: {value}")
    
    # ดาวน์โหลดโปรไฟล์ภาพ
    instagramBot.download_profile(username, profile_pic_only=True)
    
    # ย้ายไฟล์โปรไฟล์ไปยังโฟลเดอร์ของผู้ใช้
    for file in os.listdir(username):
        if ".jpg" in file:
            shutil.move(f"{username}/{file}", user_folder)
    shutil.rmtree(username)
    
    # ดาวน์โหลดโพสต์ทั้งหมด
    os.chdir(user_folder)
    if not os.path.exists("Videos"):
        os.mkdir("Videos")
    posts = profile.get_posts()
    print("กำลังดาวน์โหลด... กด Ctrl + C เพื่อหยุดการดาวน์โหลด.")
    for index, post in enumerate(posts):
        try:
            instagramBot.download_post(post, target=index)
        except KeyboardInterrupt:
            print("การดาวน์โหลดถูกยกเลิก.")
            break
    
    # การจัดระเบียบโฟลเดอร์
    for folder in os.listdir():
        if "." not in folder:
            for item in os.listdir(folder):
                if ".jpg" in item:
                    shutil.move(f"{folder}/{item}", user_folder)
                elif ".mp4" in item:
                    try:
                        shutil.move(f"{folder}/{item}", f"{user_folder}/Videos")
                    except:
                        continue
            shutil.rmtree(folder)
    print("ข้อมูลทั้งหมดของ '{0}' ถูกดาวน์โหลดเรียบร้อย.".format(username))

# ฟังก์ชันดาวน์โหลดโปรไฟล์ภาพ
def download_profile_picture():
    currentPath = os.getcwd()
    username = input("กรุณาป้อนชื่อผู้ใช้เพื่อดาวน์โหลดโปรไฟล์ภาพ: ")
    user_folder = os.path.join(currentPath, username)  # สร้างโฟลเดอร์ผู้ใช้
    if not os.path.exists(user_folder):
        os.mkdir(user_folder)
    
    instagramBot.download_profile(username, profile_pic_only=True)
    
    # ย้ายไฟล์โปรไฟล์ไปยังโฟลเดอร์ของผู้ใช้
    for file in os.listdir(username):
        if ".jpg" in file:
            shutil.move(f"{username}/{file}", user_folder)
    shutil.rmtree(username)
    print("โปรไฟล์ภาพของ '{0}' ถูกดาวน์โหลดเรียบร้อย.".format(username))

# ฟังก์ชันดาวน์โหลดโพสต์ทั้งหมด
def download_all_posts():
    currentPath = os.getcwd()
    username = input("กรุณาป้อนชื่อผู้ใช้ที่ต้องการดาวน์โหลด: ")
    try:
        profile = instaloader.Profile.from_username(instagramBot.context, username)
    except:
        print("ไม่พบชื่อผู้ใช้นี้.")
        return
    
    user_folder = os.path.join(currentPath, username)  # สร้างโฟลเดอร์ผู้ใช้
    if not os.path.exists(user_folder):
        os.mkdir(user_folder)
    
    os.chdir(user_folder)
    if not os.path.exists("Videos"):
        os.mkdir("Videos")
    posts = profile.get_posts()
    print("กำลังดาวน์โหลด... กด Ctrl + C เพื่อหยุดการดาวน์โหลด.")
    for index, post in enumerate(posts):
        try:
            instagramBot.download_post(post, target=index)
        except KeyboardInterrupt:
            print("การดาวน์โหลดถูกยกเลิก.")
            break
    
    # การจัดระเบียบโฟลเดอร์
    for folder in os.listdir():
        if "." not in folder:
            for item in os.listdir(folder):
                if ".jpg" in item:
                    shutil.move(f"{folder}/{item}", user_folder)
                elif ".mp4" in item:
                    try:
                        shutil.move(f"{folder}/{item}", f"{user_folder}/Videos")
                    except:
                        continue
            shutil.rmtree(folder)
    print("ข้อมูลทั้งหมดของ '{0}' ถูกดาวน์โหลดเรียบร้อย.".format(username))

# ฟังก์ชันดาวน์โหลดรูปภาพจากแฮชแท็ก
def download_images_from_hashtag():
    try:
        instaloader.Instaloader(download_videos=False, save_metadata=False, post_metadata_txt_pattern='').download_hashtag(input("กรุณาป้อนแฮชแท็ก: "), max_count=20)
    except KeyboardInterrupt:
        print("การดาวน์โหลดถูกยกเลิก")

# ฟังก์ชันเมนูหลัก
def main_menu():
    print("เมนูหลัก")
    myTable = PrettyTable(["ดัชนี", "งาน"])
    myTable.add_row(["1", "ดาวน์โหลดโปรไฟล์ภาพจากชื่อผู้ใช้"])
    myTable.add_row(["2", "ดาวน์โหลดโพสต์ทั้งหมดจากชื่อผู้ใช้"])
    myTable.add_row(["3", "ดาวน์โหลดข้อมูลทั้งหมดของผู้ใช้"])
    myTable.add_row(["4", "ดาวน์โหลดรูปภาพจากแฮชแท็ก"])
    myTable.add_row(["5", "ออกจากโปรแกรม"])
    print(myTable)
    return input("กรุณาป้อนดัชนีที่ต้องการทำ: ")

# ฟังก์ชันหลัก
def main():
    # เข้าสู่ระบบ
    auth()
    # ลูปเพื่อไม่ให้สคริปต์หยุดทำงาน
    while True:
        # แสดงเมนูหลัก
        query = main_menu()
        # เลือกงานตามดัชนีที่เลือก
        if query == "1":
            download_profile_picture()
        elif query == "2":
            download_all_posts()
        elif query == "3":
            download_user_data()
        elif query == "4":
            download_images_from_hashtag()
        elif query == "5":
            print("ออกจากโปรแกรม.")
            break
        else:
            print("กรุณาป้อนดัชนีที่ถูกต้อง.")

# เรียกใช้ฟังก์ชันหลัก
if __name__ == "__main__":
    main()





ให้มีการตรวจสอบป้องกันการโหลดข้อมูลซ้ำ