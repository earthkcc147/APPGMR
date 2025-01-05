import pygame, sys, time
from pygame.locals import *

# ตั้งค่า Pygame
pygame.init()

# ตั้งค่าหน้าต่าง
WIDTH = 400
HEIGHT = 400
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('แอนิเมชั่น')

# ตั้งค่าตัวแปรทิศทาง
DOWNLEFT = 'ลงซ้าย'
DOWNRIGHT = 'ลงขวา'
UPLEFT = 'ขึ้นซ้าย'
UPRIGHT = 'ขึ้นขวา'

MOVESPEED = 4

# ตั้งค่าสี
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ตั้งค่าข้อมูลของกล่อง
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 90, 60), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# รันลูปเกม
while True:
    # ตรวจสอบเหตุการณ์ Quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # วาดพื้นหลังสีขาว
    windowSurface.fill(WHITE)
    
    for b in boxes:
        # เคลื่อนที่กล่อง
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED
                
        # ตรวจสอบว่ากล่องออกจากหน้าต่างหรือไม่
        if b['rect'].top < 0:
            # ถ้ากล่องออกจากด้านบน
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > HEIGHT:
            # ถ้ากล่องออกจากด้านล่าง
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # ถ้ากล่องออกจากด้านซ้าย
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WIDTH:
            # ถ้ากล่องออกจากด้านขวา
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
                
        # วาดกล่องลงบนหน้าต่าง
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # อัปเดตหน้าต่าง
    pygame.display.update()
    time.sleep(0.02)