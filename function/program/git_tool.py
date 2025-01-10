import os
import git
import getpass

# ฟังก์ชั่นสำหรับการเข้าสู่ระบบ GitHub
def login():
    username = input("กรุณาใส่ชื่อผู้ใช้งาน GitHub: ")
    password = getpass.getpass("กรุณาใส่รหัสผ่าน GitHub: ")
    # นี่เป็นการรับค่าผู้ใช้และรหัสผ่านจากผู้ใช้ แต่ไม่ได้ตรวจสอบการเข้าสู่ระบบจริง
    print(f"เข้าสู่ระบบสำเร็จสำหรับ {username}!")
    return username, password

# ฟังก์ชั่นสำหรับการ Clone Repository
def clone_repo():
    repo_url = input("กรุณาใส่ URL ของ Repository GitHub: ")
    clone_dir = input("กรุณาใส่โฟลเดอร์ที่ต้องการโคลน Repository ไป: ")
    try:
        print(f"กำลังโคลน repository {repo_url} ไปยัง {clone_dir}...")
        repo = git.Repo.clone_from(repo_url, clone_dir)
        print(f"โคลน repository สำเร็จแล้วที่ {clone_dir}")
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการโคลน repository: {e}")

# ฟังก์ชั่นสำหรับการ Commit การเปลี่ยนแปลง
def commit_changes():
    repo_dir = input("กรุณาใส่โฟลเดอร์ของ repository ที่ต้องการ commit: ")
    commit_message = input("กรุณาใส่ข้อความสำหรับ commit: ")
    
    try:
        repo = git.Repo(repo_dir)
        repo.git.add(A=True)  # เพิ่มไฟล์ทั้งหมดที่มีการเปลี่ยนแปลง
        repo.index.commit(commit_message)  # Commit การเปลี่ยนแปลง
        print("Commit การเปลี่ยนแปลงสำเร็จ!")
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการ commit: {e}")

# ฟังก์ชั่นสำหรับการ Push ขึ้น GitHub
def push_changes():
    repo_dir = input("กรุณาใส่โฟลเดอร์ของ repository ที่ต้องการ push: ")
    
    try:
        repo = git.Repo(repo_dir)
        origin = repo.remotes.origin
        origin.push()  # Push การเปลี่ยนแปลงไปที่ GitHub
        print("Push การเปลี่ยนแปลงสำเร็จ!")
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการ push: {e}")

# ฟังก์ชั่นสำหรับการดึงข้อมูลจาก GitHub (Pull)
def pull_changes():
    repo_dir = input("กรุณาใส่โฟลเดอร์ของ repository ที่ต้องการ pull: ")
    
    try:
        repo = git.Repo(repo_dir)
        origin = repo.remotes.origin
        origin.pull()  # Pull การเปลี่ยนแปลงล่าสุดจาก GitHub
        print("Pull การเปลี่ยนแปลงสำเร็จ!")
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการ pull: {e}")

# ฟังก์ชั่นสำหรับการดูสถานะของโปรเจกต์
def status():
    repo_dir = input("กรุณาใส่โฟลเดอร์ของ repository ที่ต้องการดูสถานะ: ")
    
    try:
        repo = git.Repo(repo_dir)
        status = repo.git.status()  # ดูสถานะของ repository
        print("สถานะของ repository ปัจจุบัน:")
        print(status)
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการดูสถานะ: {e}")

# ฟังก์ชั่นสำหรับการสร้าง Branch ใหม่
def create_branch():
    repo_dir = input("กรุณาใส่โฟลเดอร์ของ repository ที่ต้องการสร้าง branch ใหม่: ")
    branch_name = input("กรุณาใส่ชื่อ branch ใหม่: ")
    
    try:
        repo = git.Repo(repo_dir)
        new_branch = repo.create_head(branch_name)  # สร้าง branch ใหม่
        new_branch.checkout()  # สลับไปที่ branch ใหม่
        print(f"สร้าง branch ใหม่ชื่อ {branch_name} และสลับไปยัง branch นี้แล้ว!")
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการสร้าง branch: {e}")

# ฟังก์ชั่นสำหรับการ Merge Branch
def merge_branch():
    repo_dir = input("กรุณาใส่โฟลเดอร์ของ repository ที่ต้องการทำการ merge: ")
    branch_to_merge = input("กรุณาใส่ชื่อ branch ที่ต้องการ merge: ")
    
    try:
        repo = git.Repo(repo_dir)
        current_branch = repo.active_branch
        repo.git.checkout(branch_to_merge)  # สลับไปที่ branch ที่ต้องการ merge
        repo.git.merge(current_branch)  # ทำการ merge
        print(f"Merge branch {branch_to_merge} เข้ากับ {current_branch} สำเร็จ!")
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการ merge: {e}")

# ฟังก์ชั่นสำหรับการลบไฟล์ที่ไม่ต้องการ
def remove_file():
    repo_dir = input("กรุณาใส่โฟลเดอร์ของ repository ที่ต้องการลบไฟล์: ")
    file_name = input("กรุณาใส่ชื่อไฟล์ที่ต้องการลบ: ")
    
    try:
        repo = git.Repo(repo_dir)
        os.remove(os.path.join(repo_dir, file_name))  # ลบไฟล์
        repo.git.add(A=True)  # เพิ่มการเปลี่ยนแปลงที่เกิดขึ้น
        repo.index.commit(f"ลบไฟล์ {file_name}")  # Commit การลบไฟล์
        print(f"ไฟล์ {file_name} ถูกลบและ commit สำเร็จ!")
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการลบไฟล์: {e}")

# ฟังก์ชั่นสำหรับการดู log ของ commit
def view_log():
    repo_dir = input("กรุณาใส่โฟลเดอร์ของ repository ที่ต้องการดู log: ")
    
    try:
        repo = git.Repo(repo_dir)
        log = repo.git.log()  # ดู log ของ commit
        print("Log ของ commit:")
        print(log)
    except git.exc.GitCommandError as e:
        print(f"เกิดข้อผิดพลาดในการดู log: {e}")

# ฟังก์ชั่นสำหรับอธิบายความสามารถของโปรแกรม
def explain_program():
    print("\n=== อธิบายความสามารถของโปรแกรม ===")
    print("โปรแกรมนี้เป็นเครื่องมือที่ใช้สำหรับควบคุมและจัดการโปรเจกต์ GitHub ผ่านคำสั่งต่างๆ ในระบบ Git ได้แก่:")
    print("1. โคลน (clone) repository จาก GitHub ลงในเครื่องของผู้ใช้")
    print("2. Commit การเปลี่ยนแปลงที่ทำในไฟล์ต่างๆ ใน repository")
    print("3. Push การเปลี่ยนแปลงที่ commit ไปยัง GitHub")
    print("4. Pull การเปลี่ยนแปลงจาก GitHub มายังเครื่องของผู้ใช้")
    print("5. ดูสถานะของ repository ว่ามีการเปลี่ยนแปลงอะไรบ้าง")
    print("6. สร้าง branch ใหม่ใน repository เพื่อการพัฒนาแยกต่างหาก")
    print("7. ทำการ merge ข้อมูลจาก branch หนึ่งเข้ากับ branch ปัจจุบัน")
    print("8. ลบไฟล์ที่ไม่ต้องการใน repository")
    print("9. ดู log ของ commit ที่ได้ทำไว้ใน repository")
    print("โปรแกรมนี้ใช้การควบคุม Git ผ่านคำสั่งต่างๆ เพื่อช่วยให้ผู้ใช้สามารถจัดการ repository ได้อย่างง่ายดาย")


def main_menu():
    # เรียกฟังก์ชั่น login ก่อน
    login()
    explain_program()

    print("\n=== เมนูหลัก ===")
    print("1. โคลน repository")
    print("2. Commit การเปลี่ยนแปลง")
    print("3. Push การเปลี่ยนแปลงไปยัง GitHub")
    print("4. Pull การเปลี่ยนแปลงจาก GitHub")
    print("5. ดูสถานะของ repository")
    print("6. สร้าง branch ใหม่")
    print("7. Merge branch")
    print("8. ลบไฟล์ที่ไม่ต้องการ")
    print("9. ดู log ของ commit")
    print("10. อธิบายความสามารถของโปรแกรม")
    print("11. ออกจากโปรแกรม")

    while True:
        choice = input("กรุณาเลือกหมายเลข (1-11): ")

        if choice == '1':
            clone_repo()
        elif choice == '2':
            commit_changes()
        elif choice == '3':
            push_changes()
        elif choice == '4':
            pull_changes()
        elif choice == '5':
            status()
        elif choice == '6':
            create_branch()
        elif choice == '7':
            merge_branch()
        elif choice == '8':
            remove_file()
        elif choice == '9':
            view_log()
        elif choice == '10':
            explain_program()
        elif choice == '11':
            print("ออกจากโปรแกรม...")
            break
        else:
            print("เลือกหมายเลขไม่ถูกต้อง กรุณาลองใหม่.")

if __name__ == "__main__":
    main_menu()