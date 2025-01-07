# สคริปต์ Python เพื่อทำให้ CPU ทำงานหนักในสภาพอากาศเย็น

from multiprocessing import Process, cpu_count
from sys import argv

# กำหนดจำนวนกระบวนการเริ่มต้นตามจำนวนคอร์ของ CPU
defaultProcessCount: int = cpu_count()
processCount: int = int(argv[1]) if len(argv) > 1 else defaultProcessCount

# ฟังก์ชันที่ทำให้ CPU ทำงานหนักเพื่อสร้างความร้อน
def heat():
    while True:  # เพิ่มลูปไม่สิ้นสุด
        for i in range(1 * 10 ** 16):
            i = i ** i

# สร้างกระบวนการให้ทำงานตามจำนวนที่ระบุ
for i in range(processCount):
    print("เริ่มกระบวนการหมายเลข:", i + 1)
    t = Process(target=heat)
    t.start()