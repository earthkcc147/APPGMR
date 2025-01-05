# นำเข้าโมดูล
import tkinter
import random

# รายการของสีที่สามารถใช้ได้
colours = ['แดง', 'น้ำเงิน', 'เขียว', 'ชมพู', 'ดำ',
           'เหลือง', 'ส้ม', 'ขาว', 'ม่วง', 'น้ำตาล']
score = 0

# เวลาที่เหลือในเกม เริ่มต้นที่ 30 วินาที
timeleft = 30

# ฟังก์ชันที่เริ่มเกม
def startGame(event):
    if timeleft == 30:
        # เริ่มจับเวลา
        countdown()
    # เรียกฟังก์ชันเพื่อเลือกสีถัดไป
    nextColour()

# ฟังก์ชันเลือกและแสดงสีถัดไป
def nextColour():
    global score
    global timeleft

    # ถ้าเกมยังเล่นอยู่
    if timeleft > 0:
        # ทำให้กล่องข้อความใช้งานได้
        e.focus_set()

        # ถ้าคำที่พิมพ์ตรงกับสีที่แสดง
        if e.get().lower() == colours[1].lower():
            score += 1

        # เคลียร์กล่องข้อความ
        e.delete(0, tkinter.END)

        # สับเปลี่ยนสีในรายการ
        random.shuffle(colours)

        # เปลี่ยนสีของคำที่แสดง
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # อัพเดตคะแนน
        scoreLabel.config(text="คะแนน: " + str(score))

# ฟังก์ชันจับเวลาถอยหลัง
def countdown():
    global timeleft

    # ถ้าเกมยังเล่นอยู่
    if timeleft > 0:
        # ลดเวลาลงทีละ 1
        timeleft -= 1

        # อัพเดตเวลาที่เหลือ
        timeLabel.config(text="เวลาที่เหลือ: " + str(timeleft))

        # เรียกฟังก์ชันนี้อีกครั้งหลังจาก 1 วินาที
        timeLabel.after(1000, countdown)

# โค้ดหลัก

# สร้างหน้าต่าง GUI
root = tkinter.Tk()

# ตั้งชื่อหน้าต่าง
root.title("เกมสี")

# ตั้งขนาดหน้าต่าง
root.geometry("375x200")

# เพิ่มป้ายคำแนะนำ
instructions = tkinter.Label(root, text="พิมพ์ชื่อสีของคำที่แสดง ไม่ใช่สีของคำ",
                             font=('Helvetica', 12))
instructions.pack()

# เพิ่มป้ายแสดงคะแนน
scoreLabel = tkinter.Label(root, text="กด Enter เพื่อเริ่มเกม",
                           font=('Helvetica', 12))
scoreLabel.pack()

# เพิ่มป้ายแสดงเวลาที่เหลือ
timeLabel = tkinter.Label(root, text="เวลาที่เหลือ: " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()

# เพิ่มป้ายแสดงสี
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# เพิ่มกล่องข้อความสำหรับพิมพ์สี
e = tkinter.Entry(root)

# เรียกฟังก์ชัน 'startGame' เมื่อกดปุ่ม Enter
root.bind('<Return>', startGame)
e.pack()

# ตั้งโฟกัสให้กับกล่องข้อความ
e.focus_set()

# เริ่มการทำงานของ GUI
root.mainloop()