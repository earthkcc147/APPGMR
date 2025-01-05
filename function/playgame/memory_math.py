# นำเข้าคลาสและฟังก์ชันที่จำเป็น
from random import *
from turtle import *
from freegames import path


# สร้างแพลตฟอร์มที่มี 64 ช่อง
car = path("car.gif")
tiles = list(range(32)) * 2
state = {"mark": None}
hide = [True] * 64


# สร้างฟังก์ชันสำหรับการวาดสี่เหลี่ยม
def square(x, y):
    "วาดสี่เหลี่ยมสีขาวขอบดำที่ตำแหน่ง (x, y)"
    up()
    goto(x, y)
    down()
    # กำหนดสีของสี่เหลี่ยม
    color("black", "white")
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "แปลงพิกัด (x, y) เป็นดัชนีของ tiles"
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "แปลงจำนวนของ tiles เป็นพิกัด (x, y)"
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    "อัปเดต mark และช่องที่ซ่อนไว้ตามการแตะ"
    spot = index(x, y)
    mark = state["mark"]

    # แสดงบนหน้าจอถ้าหมายเลขที่เลือกสองตัวตรงกัน
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state["mark"] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state["mark"] = None


def draw():
    "วาดภาพและ tiles"
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state["mark"]

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color("black")
        write(tiles[mark], font=("Arial", 30, "normal"))

    update()
    ontimer(draw, 100)


# สับเปลี่ยน tiles
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()