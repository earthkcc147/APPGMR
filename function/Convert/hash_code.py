import hashlib
import os

# แผนที่ของวิธีการแฮชที่สามารถใช้งานได้
HASH_MAP = {
    "--md5": hashlib.md5,
    "--sha1": hashlib.sha1,
    "--sha224": hashlib.sha224,
    "--sha256": hashlib.sha256,
    "--sha384": hashlib.sha384,
    "--sha512": hashlib.sha512,
    "--blake2b": hashlib.blake2b,
    "--blake2s": hashlib.blake2s,
    "--sha3_224": hashlib.sha3_224,
    "--sha3_256": hashlib.sha3_256,
    "--sha3_384": hashlib.sha3_384,
    "--sha3_512": hashlib.sha3_512,
    "--shake_128": hashlib.shake_128,
    "--shake_256": hashlib.shake_256,
}

# ฟังก์ชันแสดงวิธีการใช้งาน
def help():
    print("วิธีใช้งาน: python main.py [--<method>] filenames")
    print("วิธีการแฮชที่สามารถใช้ได้")
    for method in HASH_MAP:
        print("   ", method)

# ฟังก์ชันหลักของโปรแกรม
def main():
    while True:
        # เมนูหลัก
        print("\n--- เมนูหลัก ---")
        print("1. เลือกวิธีการแฮช")
        print("2. ออกจากโปรแกรม")
        choice = input("กรุณาเลือกตัวเลือก (1/2): ").strip()

        if choice == "1":
            flag = input("กรุณากรอกวิธีการแฮช (--md5, --sha256, etc.): ").strip()
            if flag == "":
                flag = "--md5"  # ถ้าไม่กรอกจะใช้ md5 เป็นค่าเริ่มต้น

            if flag == "--help":
                help()
                continue

            try:
                hsh = HASH_MAP[flag]
            except KeyError:
                print("วิธีการแฮชที่เลือกไม่ถูกต้อง:", flag)
                help()
                continue

            # รับชื่อไฟล์จากผู้ใช้ (รองรับการลากและวางไฟล์)
            print("สามารถลากและวางไฟล์ในช่องนี้ หรือพิมพ์พาธไฟล์ได้")
            filenames_input = input("กรุณากรอกหรือวางชื่อไฟล์ (คั่นด้วยช่องว่าง): ").strip()
            filenames = filenames_input.split()  # แยกชื่อไฟล์ตามช่องว่าง

            if len(filenames) == 0:
                help()
                continue

            # อ่านไฟล์และคำนวณแฮช
            for filename in filenames:
                filename = filename.strip('"')  # ลบเครื่องหมายคำพูดออกในกรณีลากไฟล์มา
                if not os.path.isfile(filename):
                    print(f"ไม่พบไฟล์: {filename}")
                    continue

                try:
                    with open(filename, "r", encoding="utf-8") as fd:
                        content = fd.read()
                        m = hsh(str.encode(content))
                        print(f"{m.hexdigest()}  {filename}")
                except Exception as e:
                    print(f"เกิดข้อผิดพลาดในการอ่านไฟล์ {filename}: {e}")
        
        elif choice == "2":
            print("ขอบคุณที่ใช้โปรแกรม! ลาก่อน!")
            break  # ออกจากโปรแกรม

        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")

# เรียกใช้งานฟังก์ชันหลัก
if __name__ == "__main__":
    main()