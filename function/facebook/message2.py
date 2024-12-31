import time
import pyperclip
import subprocess
import sys

# ตรวจสอบว่าโมดูล selenium และ pyperclip ถูกติดตั้งหรือยัง
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# ตรวจสอบและติดตั้ง selenium และ pyperclip ถ้ายังไม่มี
try:
    import selenium
except ImportError:
    install_package('selenium')

try:
    import pyperclip
except ImportError:
    install_package('pyperclip')

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------ ข้อมูลผู้ใช้  ------------------ #

email_id = input('กรุณากรอกอีเมลของคุณ: ')
password = input('กรุณากรอกรหัสผ่านของคุณ: ')

page_link = input('กรุณากรอกลิงก์หน้า Facebook ที่จะทำการสแปม: ')
number_of_times = int(input('กรุณากรอกจำนวนครั้งที่ต้องการสแปม: '))
frequency = int(input('กรุณากรอกความถี่ในการสแปม (จำนวนครั้งที่ส่งในแต่ละครั้ง): '))
message = input('กรุณากรอกข้อความที่ต้องการสแปม: ')

# ----------------- เริ่มต้นการใช้งาน CHROMEDRIVER  ---------------------- #

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"  # เปิดการรอคอยแบบเจาะจง
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # เปิด Chrome แบบเต็มหน้าจอ
options.add_argument('--disable-notifications')
url = 'https://www.facebook.com'
driver = webdriver.Chrome('E:\Python\chromedriver.exe', desired_capabilities=capa, chrome_options=options)  # ตัวเลือก
driver.get(url)

# ----------------- ล็อกอินและเริ่มทำการสแปม  ----------------- #

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.ID, "email")))
driver.find_element_by_id('email').send_keys(email_id)  # ใส่อีเมล
driver.find_element_by_id('pass').send_keys(password)  # ใส่รหัสผ่าน
driver.find_element_by_xpath("//input[@value='Log In']").click()  # คลิกเพื่อเข้าสู่ระบบ

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
driver.get(page_link)  # ไปที่หน้าหรือโปรไฟล์ที่ต้องการ
time.sleep(10)

''' เลื่อนหน้าจอลงไปจนกว่าจะมีโพสต์ที่สามารถคอมเมนต์ได้มากกว่าหรือเท่ากับจำนวนที่กำหนด '''
comment_boxes = driver.find_elements_by_xpath("//div[text()='Write a comment...']")
while len(comment_boxes) < number_of_times:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        pass
    comment_boxes = driver.find_elements_by_xpath("//div[text()='Write a comment...']")

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")  # เลื่อนกลับไปที่ด้านบนของหน้า
time.sleep(5)
original = len(driver.find_elements_by_xpath("//div[text()='Write a comment...']"))  # ติดตามจำนวนโพสต์
pyperclip.copy(message)  # คัดลอกข้อความไปยังคลิปบอร์ด

actions = ActionChains(driver)  # สร้าง ActionChains
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER)  # กด Ctrl+V

for i in range(0, number_of_times):
    for j in range(0, frequency):
        comment_boxes = driver.find_elements_by_xpath("//div[text()='Write a comment...']")  # ค้นหาช่องคอมเมนต์
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", comment_boxes[i])  # เลื่อนเพื่อให้เห็นช่องคอมเมนต์
        time.sleep(2)
        driver.execute_script("arguments[0].click();", comment_boxes[i])  # คลิกที่ช่องคอมเมนต์

        check = True
        while check is True:
            try:
                comment_boxes = driver.find_elements_by_xpath("//div[text()='Write a comment...']")
                if comment_boxes[i].find_element_by_xpath('..').value_of_css_property('color') == \
                        'rgba(190, 195, 201, 1)':
                    check = False
            except:
                pass

        actions.perform()  # ทำการกด Ctrl+V
        ''' ทำการคอมเมนต์ถัดไปเมื่อคอมเมนต์ก่อนหน้านี้เสร็จแล้วเท่านั้น. '''
        while len(driver.find_elements_by_xpath("//div[text()='Write a comment...']")) < original:
            time.sleep(0.5)

    print(str(i+1), "/", str(number_of_times), "โพสต์ที่ถูกสแปม.")