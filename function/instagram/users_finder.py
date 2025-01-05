import hashlib, json, re, requests
import os  # ใช้สำหรับตรวจสอบไฟล์และสร้างไฟล์

authtokens = tuple()

def checkTokens():
    if not authtokens:
        getTokens()

def getTokens():
    r = requests.get('https://instagram.com/', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0', }).text
    rhx_gis = json.loads(re.compile('window._sharedData = ({.*?});', re.DOTALL).search(r).group(1))['nonce']

    ppc = re.search(r'ConsumerLibCommons.js/(.*?).js', r).group(1)
    r = requests.get('https://www.instagram.com/static/bundles/metro/ConsumerLibCommons.js/' + ppc + '.js').text
    query_hash = re.findall(r'{value:!0}\);(?:var|const|let) .=\"([0-9a-f]{32})\"', r)[1]

    global authtokens
    authtokens = tuple((rhx_gis, query_hash))

def const_gis(query):
    checkTokens()
    t = authtokens[0] + ':' + query
    x_instagram_gis = hashlib.md5(t.encode("utf-8")).hexdigest()
    return x_instagram_gis

def usernameToUserId(user):
    r = requests.get('https://www.instagram.com/web/search/topsearch/?query=' + user, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}).text

    if json.loads(r).get("message") == 'rate limited':
        print(
            '[x] เกินขีดจำกัดแล้ว!\n[#] ไม่สามารถตรวจสอบชื่อผู้ใช้: {}\n[!] กรุณาลองใหม่ในไม่กี่นาที.\n'.format(user))
        exit()

    try:
        for i in range(len(json.loads(r)['users'])):
            if json.loads(r)['users'][i]['user']['username'] == user:
                return json.loads(r)['users'][i]['user']['pk']
    except IndexError:
        return False

def useridToUsername(userid):
    header = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 12.0.0.16.90 (iPhone9,4; iOS 10_3_3; en_US; en-US; scale=2.61; gamut=wide; 1080x1920)',
        'X-Requested-With': 'XMLHttpRequest'}
    r = requests.get(
        f'https://i.instagram.com/api/v1/users/{userid}/info/',
        headers=header)

    if r.status_code == 404:
        return False

    j = json.loads(r.text)

    if j.get("status") != 'ok':
        print('[x] เกินขีดจำกัดแล้ว!\n[#] ไม่สามารถตรวจสอบ UserID: {}\n[!] กรุณาลองใหม่ในไม่กี่นาที..\n'.format(userid))
        exit()
    try:
        return j['user']['username']
    except IndexError:
        return False

def create_sample_file():
    # ตรวจสอบว่าไฟล์ users.txt มีอยู่แล้วหรือไม่ ถ้าไม่มีจะสร้างใหม่พร้อมข้อมูลตัวอย่าง
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w') as file:
            file.write('username1\n')
            file.write('username2\n')
            file.write('username3\n')
            print('[+] สร้างไฟล์ users.txt และเพิ่มข้อมูลตัวอย่างแล้ว')

def main():
    create_sample_file()  # สร้างไฟล์ users.txt และเพิ่มข้อมูลตัวอย่าง

    print("เลือกตัวเลือกในการค้นหาข้อมูล Instagram:")
    print("1. ค้นหาจากชื่อผู้ใช้ (Username)")
    print("2. ค้นหาจาก UserID")
    print("3. ค้นหาหลายรายการจากไฟล์ .txt")
    choice = input("กรุณากรอกหมายเลขตัวเลือก (1/2/3): ")

    if choice == '1':
        username = input("กรุณากรอกชื่อผู้ใช้ Instagram: ")
        userid = usernameToUserId(username)
        if not userid:
            print('[-] ชื่อผู้ใช้ไม่มีอยู่จริง')
        else:
            print('[+] UserID: {}'.format(userid))

    elif choice == '2':
        userid = int(input("กรุณากรอก UserID ของ Instagram: "))
        username = useridToUsername(userid)
        if not username:
            print('[-] UserID ไม่มีอยู่จริง')
        else:
            print('[+] ชื่อผู้ใช้: {}'.format(username))

    elif choice == '3':
        file_path = 'users.txt'  # ใช้ไฟล์ users.txt ที่สร้างขึ้นอัตโนมัติ
        result = list()

        try:
            with open(file_path, 'r') as file:
                elements = file.readlines()
        except FileNotFoundError:
            print('[-] ไม่พบไฟล์ :(')
            return 0

        print("กำลังประมวลผล...\n")
        # ตรวจสอบการมีอยู่ของไฟล์ result.txt ถ้าไม่มีก็จะสร้างใหม่
        if not os.path.exists('result.txt'):
            with open('result.txt', 'w') as file:
                pass  # สร้างไฟล์ result.txt ถ้ายังไม่มี

        with open('result.txt', 'w') as file:
            for e in elements:
                e = e.strip()
                if e.isdigit():
                    username = useridToUsername(e)
                    if username:
                        result.append('{}:{}'.format(e, username))
                        file.write('{}:{}\n'.format(e, username))
                    else:
                        print('[-] "{}" ไม่พบ!\n'.format(e))
                else:
                    userid = usernameToUserId(e)
                    if userid:
                        result.append('{}:{}'.format(userid, e))
                        file.write('{}:{}\n'.format(userid, e))
                    else:
                        print('[-] "{}" ไม่พบ!\n'.format(e))

        print('[++] บันทึกผลลัพธ์เป็น result.txt')
    else:
        print("ตัวเลือกไม่ถูกต้อง!")

if __name__ == '__main__':
    main()