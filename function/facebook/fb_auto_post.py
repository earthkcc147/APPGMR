from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import getpass

try:
    driver = webdriver.Chrome(
        "<===============ENTER YOUR CHROME DRIVER PATH===========>"
    )
    driver.get("https://www.facebook.com/")
    print("Facebook เปิดสำเร็จ...!")
    time.sleep(5)

    # กรอกอีเมล
    facebookEmail = input("กรุณากรอกอีเมลของคุณ: ")
    email = driver.find_element(By.XPATH, "//input[@id='email' or @name='email']")
    email.send_keys(facebookEmail)
    print("อีเมลกรอกสำเร็จ")

    # กรอกรหัสผ่าน
    facebookPassword = getpass.getpass("กรุณากรอกรหัสผ่านของ Facebook: ")
    password = driver.find_element(By.XPATH, "//input[@id='pass']")
    password.send_keys(facebookPassword)
    print("รหัสผ่านกรอกสำเร็จ")

    # คลิกปุ่มเข้าสู่ระบบ
    button = driver.find_element(By.XPATH, "//input[@id='u_0_r']")
    button.click()
    print("เข้าสู่ระบบสำเร็จ")
    time.sleep(15)

    # โพสต์ข้อความ
    inputbox = driver.find_element(By.CSS_SELECTOR, "span._5qtp")
    inputbox.click()
    time.sleep(5)

    Text = input("\tอยากบอกอะไร? เขียนความคิดของคุณที่นี่: \n")
    text = driver.find_element(By.CSS_SELECTOR, "#composer_text_input_box")
    text.click()
    text.send_keys(Text)

    postbutton = driver.find_element(By.XPATH, "//*[text()='โพสต์']")
    postbutton.click()
    time.sleep(15)
    
    print("โพสต์สำเร็จ!")
    driver.close()

except NoSuchElementException as e:
    print(f"ไม่พบองค์ประกอบที่ระบุ: {e}")
except Exception as e:
    print(f"เกิดข้อผิดพลาดบางประการ: {e}")