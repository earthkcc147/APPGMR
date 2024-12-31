import re
import random
import getpass
try:
    import bs4
    import mechanize
except:
    print("[!] กรุณาติดตั้ง mechanize & bs4 ก่อนนะครับ")
    print("[*] ถ้าไม่รู้วิธีติดตั้งคำสั่ง: pip2 install mechanize; pip2 install bs4")

_RAHIM = ""
_TARGETS = ""
_RAHIMIBU = 0

print("""
+++++++++++++++++++
 บอทแชท Facebook
 +++++++++++++++++
 Recode By X-Mr.R4h1M
+++++++++++++++++++
""")
class SPAMMER:
    def __init__(self):
        self.br=mechanize.Browser()
        self.br.set_handle_equiv(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)
        self.br.addheaders = [
            (
                "User-Agent",
                "Mozilla/5.1 (Linux Android)"
            )]
        self._url="https://mbasic.facebook.com/"
        print("[*] กรุณาล็อกอินเข้าสู่ Facebook ของคุณ")
        self._email = raw_input("[*] อีเมล : ")
        self._pasw = getpass.getpass("[*] รหัสผ่าน: ")
        print("[+] กำลังพยายามเข้าสู่ระบบ ...")
        self.login()

    def login(self):
            self.br.open("https://mbasic.facebook.com")
            self.br.select_form(nr=0)
            self.br.form["email"] = "{}".format(self._email)
            self.br.form["pass"]  ="{}".format(self._pasw)
            self.br.submit()
            if "save-device" in self.br.geturl():
                print("[*] เข้าสู่ระบบสำเร็จ ...")
                self._generateTarget()
            else:
                print("[!] ล็อกอินล้มเหลว")
                exit()

    def _generateTarget(self):
        global _TARGETS,_RAHIM
        _targ=raw_input("[*] กรอกชื่อผู้ใช้เป้าหมาย: ")
        _TARGETS=self._url+_targ
        self.br.open(_TARGETS)
        self.r=re.findall('<head><title>(.*?)</title>',
        self.br.response().read())
        if len(self.r) !=0:
            print("[*] ชื่อเป้าหมาย: \033[1;37m\033[31m%s\033[0m"%(self.r[0]))
        else:
            print("[!] ไม่พบข้อมูลเป้าหมาย")
            return self._generateTarget()
        self._counts=input("[+] จำนวนที่ต้องการส่ง: ")
        self.br.open(_TARGETS)
        _bs = self.br.response().read()
        _b=bs4.BeautifulSoup(_bs,
                features="html.parser"
            )
        for x in _b.find_all("a",href=True):
            if "/messages/thread/" in x["href"]:
                _RAHIM=x["href"]
        return self.inputMessages()

    def inputMessages(self):
        global _RAHIMIBU
        print("[*] ตัวอย่างการใช้: ข้อความจากบอท")
        _msg=raw_input("[+] ข้อความ: ").split(",")
        print("[+] เริ่มต้นการส่งข้อความ!")
        print("[+] กำลังส่ง %s ข้อความไปยัง \033[1;37m\033[31m%s\033[0m"%(
        self._counts,self.r[0]))
        for x in range(self._counts):
            ms=random.choice(_msg)
            self.br.open(_RAHIM)
            self.br._factory.is_html=True
            try:
                self.br.select_form(nr=1)
                self.br.form["body"] = "{}".format(ms)
                self.br.submit()
            except:
                print("[:'(] โอ้ยพี่ ไม่สามารถส่งข้อความได้")
                exit()
            _res=self.br.response().read()
            _RAHIMIBU+=1
            if len(re.findall(r"{}".format(ms),_res)) !=0:
                print(" | \033[1;32m{} -> ส่งแล้ว [{}]\033[0m".format(
                ms,_RAHIMIBU))
            else:
                print(" | \033[1;37m\033[31m{} -> ส่งไม่สำเร็จ [{}]\033[0m".format(
                ms,_RAHIMIBU))
        print("[+] การทำงานเสร็จสิ้น.")

if __name__ == "__main__":
    SPAMMER()