import hashlib
import sys

def main(text, hashType):
    encoder = text.encode("utf_8")
    myHash = ""

    if hashType.lower() == "md5":
        myHash = hashlib.md5(encoder).hexdigest()
    elif hashType.lower() == "sha1":
        myHash = hashlib.sha1(encoder).hexdigest()
    elif hashType.lower() == "sha224":
        myHash = hashlib.sha224(encoder).hexdigest()
    elif hashType.lower() == "sha256":
        myHash = hashlib.sha256(encoder).hexdigest()
    elif hashType.lower() == "sha384":
        myHash = hashlib.sha384(encoder).hexdigest()
    elif hashType.lower() == "sha512":
        myHash = hashlib.sha512(encoder).hexdigest()
    else:
        print("[!] สคริปต์ไม่รองรับประเภทแฮชนี้")
        sys.exit(0)
    print("แฮชของคุณคือ: ", myHash)


if __name__ == "__main__":
    text = input("กรุณากรอกข้อความที่ต้องการแฮช: ")
    hashType = input("กรุณากรอกประเภทของแฮช (เช่น md5, sha1, sha256, sha512): ")

    main(text, hashType)