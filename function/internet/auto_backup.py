import gzip
import os
import shutil
import threading


def get_input():
    """รับข้อมูลจากผู้ใช้แทนการใช้ argparse"""
    target = input("กรุณากรอกโฟลเดอร์เป้าหมายที่ต้องการสำรองข้อมูล: ")
    source = input("กรุณากรอกโฟลเดอร์/ไฟล์ต้นทาง (หากมีหลายรายการแยกด้วยช่องว่าง): ").split()
    compress = input("กรุณากรอกขนาดไฟล์ที่ต้องการบีบอัด (ในหน่วยไบต์, ค่าเริ่มต้น 1024000): ")
    
    # ใช้ค่าดีฟอลต์ถ้าผู้ใช้ไม่ได้กรอก
    if compress == "":
        compress = 1024000
    else:
        compress = int(compress)

    return target, source, compress


def size_if_newer(source, target):
    """หากไฟล์ต้นทางใหม่กว่าปลายทางจะคืนขนาดไฟล์ ไม่เช่นนั้นจะคืน False"""
    src_stat = os.stat(source)
    try:
        target_ts = os.stat(target).st_mtime
    except FileNotFoundError:
        try:
            target_ts = os.stat(target + ".gz").st_mtime
        except FileNotFoundError:
            target_ts = 0

    return src_stat.st_size if (src_stat.st_mtime - target_ts > 1) else False


def threaded_sync_file(source, target, compress):
    """การซิงค์ไฟล์ด้วยเธรด"""
    size = size_if_newer(source, target)

    if size:
        thread = threading.Thread(
            target=transfer_file, args=(source, target, size > compress)
        )
        thread.start()
        return thread


def sync_file(source, target, compress):
    """การซิงค์ไฟล์แบบไม่ใช้เธรด"""
    size = size_if_newer(source, target)

    if size:
        transfer_file(source, target, size > compress)


def transfer_file(source, target, compress):
    """คัดลอกหรือบีบอัดไฟล์"""
    try:
        if compress:
            with gzip.open(target + ".gz", "wb") as target_fid:
                with open(source, "rb") as source_fid:
                    target_fid.writelines(source_fid)
            print(f"บีบอัดไฟล์ {source}")
        else:
            shutil.copy2(source, target)
            print(f"คัดลอกไฟล์ {source}")
    except FileNotFoundError:
        os.makedirs(os.path.dirname(target))
        transfer_file(source, target, compress)


def sync_root(root, target, compress):
    """ทำการซิงค์ไฟล์จากโฟลเดอร์ต้นทางไปยังปลายทาง"""
    threads = []

    for path, _, files in os.walk(root):
        for source in files:
            source_path = os.path.join(path, source)
            target_path = os.path.join(target, path, source)
            threads.append(threaded_sync_file(source_path, target_path, compress))

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    target, source, compress = get_input()
    
    print("------------------------- เริ่มต้นการคัดลอก -------------------------")
    print("______________________________________________________________")
    
    for root in source:
        sync_root(root, target, compress)
    
    print("______________________________________________________________")
    print("------------------------- เสร็จสิ้นการสำรองข้อมูล -------------------------")