#!/usr/bin/env python3

import requests
from github import Github

# ฟังก์ชันสำหรับดึงชื่อของทุก Repository
def repository_names(user):
    repo_names = []
    for repo in user.get_repos():
        repo_names.append(repo)  # เพิ่ม Repository ลงในลิสต์
    return repo_names


# ฟังก์ชันสำหรับดึงรายละเอียดของทุก Repository
def repository_details(user):
    all_repo_details = []
    repo_names = repository_names(user)
    for repo in repo_names:
        repo_details = {}
        repo_details["ชื่อ"] = repo.full_name.split("/")[1]  # ชื่อ Repository
        repo_details["คำอธิบาย"] = repo.description  # คำอธิบาย Repository
        repo_details["สร้างเมื่อ"] = repo.created_at  # วันที่สร้าง Repository
        repo_details["ภาษาโปรแกรม"] = repo.language  # ภาษาโปรแกรมที่ใช้ใน Repository
        repo_details["ถูก Fork"] = str(repo.forks) + " ครั้ง"  # จำนวนครั้งที่ถูก Fork
        all_repo_details.append(repo_details)  # เพิ่มข้อมูล Repository ลงในลิสต์
    return all_repo_details


# เมนูหลัก
def main_menu():
    while True:
        print("\n--- เมนูหลัก ---")
        print("1. ค้นหาข้อมูล Repository")
        print("2. ออกจากโปรแกรม")
        choice = input("กรุณาเลือกตัวเลือก (1/2): ").strip()

        if choice == "1":
            username = input("\nกรุณากรอกชื่อผู้ใช้งาน GitHub: ").strip()

            if not username:
                print("ชื่อผู้ใช้งานไม่สามารถเว้นว่างได้")
                continue

            try:
                user = Github().get_user(username)  # ดึงข้อมูลผู้ใช้จาก GitHub
                RD = repository_details(user)  # ดึงรายละเอียดของ Repository

                if RD:
                    print("\n--- รายละเอียด Repository ---")
                    for content in RD:
                        for title, description in content.items():
                            print(title, ":", description)
                        print(
                            "\n-------------------------------------------------------------------------------------------------------------------\n"
                        )
                else:
                    print(f"\nผู้ใช้งาน {username} ไม่มี Repository")
            except Exception as e:
                print("\nเกิดข้อผิดพลาด:", e)

        elif choice == "2":
            print("ขอบคุณที่ใช้โปรแกรม! ลาก่อน!")
            break  # ออกจากโปรแกรม

        else:
            print("\nตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")


# เรียกใช้งานฟังก์ชันเมนูหลัก
if __name__ == "__main__":
    main_menu()