__author__ = "Sri Manikanta Palakollu"
__date__ = "08-07-2020"

import base64
import json
import time
import os


def b64_encode(source_filepath):
    # กำหนดตำแหน่งโฟลเดอร์ ImageData อยู่ในตำแหน่งเดียวกับไฟล์หลัก
    base_path = os.path.dirname(__file__)
    image_data_path = os.path.join(base_path, "ImageData")

    # ตรวจสอบว่าไดเรกทอรี 'ImageData' มีหรือไม่ ถ้าไม่มีก็จะสร้าง
    if not os.path.exists(image_data_path):
        os.makedirs(image_data_path)

    # กำหนดตำแหน่งไฟล์ encodeData.json
    encode_file_path = os.path.join(image_data_path, "encodeData.json")

    # ตรวจสอบว่าไฟล์ 'encodeData.json' มีอยู่หรือไม่
    if not os.path.exists(encode_file_path):
        # ถ้าไม่มีไฟล์ให้สร้างไฟล์ใหม่พร้อมข้อมูลเริ่มต้น
        with open(encode_file_path, "w") as f:
            json.dump({}, f)

    # อ่านข้อมูลจากไฟล์ 'encodeData.json'
    with open(encode_file_path, "r") as f:
        flag = json.loads(f.read())

    # สร้างคีย์ใหม่จากเวลา
    key = (str(int(time.time()))).encode("utf-8")

    # อ่านไฟล์รูปภาพและเข้ารหัส
    with open(source_filepath, "rb") as f:
        data = f.read()

    # ข้อมูลที่ถูกเข้ารหัส
    d = {
        "data": base64.b64encode(data).decode("utf-8"),
        "ext": source_filepath[source_filepath.index("."):],
    }

    # เพิ่มข้อมูลที่เข้ารหัสลงใน flag
    flag[key] = d

    # เขียนข้อมูลลงไฟล์ 'encodeData.json'
    with open(encode_file_path, "w") as f:
        json.dump(flag, f)

    return key


def b64_decode(key, dest_path):
    # กำหนดตำแหน่งโฟลเดอร์ ImageData อยู่ในตำแหน่งเดียวกับไฟล์หลัก
    base_path = os.path.dirname(__file__)
    image_data_path = os.path.join(base_path, "ImageData")

    # อ่านข้อมูลจากไฟล์ 'encodeData.json'
    encode_file_path = os.path.join(image_data_path, "encodeData.json")
    with open(encode_file_path, "r") as source:
        flag = json.loads(source.read())

    # คำนวณชื่อไฟล์ที่ต้องการบันทึก
    name = key + str(flag[key]["ext"])
    with open(dest_path + name, "wb") as dest:
        dest.write(base64.b64decode((flag[key]["data"]).encode("utf-8")))

    return dest_path + name


def main_menu():
    while True:
        print("\n==== เมนูหลัก ====")
        print("1. เข้ารหัสรูปภาพ")
        print("2. ถอดรหัสรูปภาพ")
        print("3. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1/2/3): ")

        if choice == "1":
            image_encode = input("กรุณากรอกพาธของไฟล์รูปภาพที่ต้องการเข้ารหัส: ")
            if image_encode:
                print("คีย์ที่ใช้ในการเข้ารหัส: {}".format(b64_encode(image_encode)))
            else:
                print("ไม่สามารถเข้ารหัสได้ เนื่องจากไม่มีไฟล์.")
        
        elif choice == "2":
            key = input("กรุณากรอกคีย์สำหรับการถอดรหัส: ")
            image_decode = input("กรุณากรอกพาธที่จะบันทึกไฟล์ที่ถอดรหัส: ")
            try:
                print("ไฟล์ถอดรหัสเสร็จสิ้น: {}".format(b64_decode(key, image_decode)))
            except Exception:
                print("เกิดข้อผิดพลาดบางประการในกระบวนการถอดรหัส..!")
        
        elif choice == "3":
            print("ออกจากโปรแกรม...")
            break
        
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่.")

# เรียกใช้เมนูหลัก
main_menu()