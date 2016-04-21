#V2.2.0 2016/4/21 12:01
#author: XenK0u
#email: xfkencpn@gmail.com
#website: http://henbukexue.science
#project website: http://fuckty.ml
import urllib2
import time
import json
import platform
import os

print '-------------------------------------------'
print 'Powered by XenK0u http://henbukexue.science'
print '-------------------------------------------'
print

user="fs1606488"#your TIANYI account
password="81719619"#your password
ISOTIMEFORMAT='%Y-%m-%d %X'
nasip="219.128.230.1"
wifi="4060"# 1050
url="http://enet.10000.gd.cn:10001/client/"
login = url + "login"
challenge = url + "challenge"
active="http://enet.10000.gd.cn:8001/hbservice/client/active?"
secret="Eshore!@#"
testurl="http://10000.gd.cn"
ua='Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'

def get_ip():
	if platform.system() == "Windows":
		import socket
		ipList = socket.gethostbyname_ex(socket.gethostname())
		for i in ipList[2]:
			if i.split('.')[0] == "10":
				return i
	ip=os.popen(". /lib/functions/network.sh; network_get_ipaddr ip wan; echo $ip").read()
	ip2=str(ip).split("\n")[0]
	return ip2

def get_mac():
	if platform.system() == "Windows":
		import uuid
		mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
		return "-".join([mac[e:e+2] for e in range(0,11,2)]).upper()
	ic=os.popen("ifconfig |grep -B1 \'"+ clientip +"\' |awk \'/HWaddr/ { print $5 }\'").read()
	ic=str(ic).split("\n")[0]
	ic=ic.replace(":","-")
	return ic.upper()

clientip = get_ip()
mac = get_mac()
print "Your IP: " + clientip
print "Your MAC: " + mac
print '-------------------------------------------'

def getmd5(str):
	import hashlib
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

def encoding(data):
	types = ['utf-8','gb2312','gbk','iso-8859-1']
	for type in types:
		try:
			return data.decode(type)
		except:
			pass
		return None

def GetTime():
	return  int((time.time()*1000))/1

def challange_http_post():
		timestr=str(GetTime())
		str1=str(clientip+nasip+mac+timestr+secret)
		md5str=getmd5(str1).upper()
		url=challenge
		values ={"username":user,"clientip":clientip,"nasip":nasip,"mac":mac,"iswifi":wifi,"timestamp":timestr,"authenticator":md5str}
		jdata = json.dumps(values)
		req = urllib2.Request(url, jdata)
		req.add_header('User-agent', ua)
		try:
			response = urllib2.urlopen(req)
			return response.read()
		except urllib2.HTTPError, e:
			print Now_time()+str(e.code)
			print Now_time()+ str(e.reason)
			return "x"
		except urllib2.URLError,e:
			print Now_time()+ str(e.reason)
			return "x"

def getToken(re):
	if (re!="x"):
		re = re.split("\",\"")[0]
		re = re.split("\":\"")[-1]
		print Now_time()+"login code is "+re
		time.sleep(1)
		return re
	else:
		return "x"

def Now_time():
	t1=time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
	str="["+t1+"] "
	return str

def login_http_post(token):
		timestr=str(GetTime())
		str1=str(clientip+nasip+mac+timestr+token+secret)
		md5str=getmd5(str1).upper()
		print Now_time()+"login..."
		url=login
		values ={"username":user,"password":password,"verificationcode":"","clientip":clientip,"nasip":nasip,"mac":mac,"iswifi":wifi,"timestamp":timestr,"authenticator":md5str}
		jdata = json.dumps(values)
		req = urllib2.Request(url, jdata)
		req.add_header('User-agent',ua)
		try:
			response = urllib2.urlopen(req)
			return response.read()
		except urllib2.HTTPError, e:
			print Now_time()+str(e.code)
			print Now_time()+ str(e.reason)
			return "x"
		except urllib2.URLError,e:
			print Now_time()+ str(e.reason)
			return "x"

def active_http_post():
	timestr=str(GetTime())
	str1=str(clientip+nasip+mac+timestr+secret)
	md5str=getmd5(str1).upper()
	url=active+"username="+user+"&clientip="+clientip+"&nasip="+nasip+"&mac="+mac+"&timestamp="+timestr+"&authenticator="+md5str
	req = urllib2.Request(url)
	req.add_header('User-agent', ua)
	try:
		response = urllib2.urlopen(req)
		return response.read()
	except urllib2.HTTPError, e:
		print Now_time()+str(e.code)
		print Now_time()+ str(e.reason)
		return "x"
	except urllib2.URLError,e:
		print Now_time()+ str(e.reason)
		return "x"

def loginl():
	str2=""
	while 1:
		ls=login_http_post(getToken(challange_http_post()))
		print Now_time()+encoding(ls)
		if (ls !="x"):
			str2=ls.split('\"')[3]
			if(str2=="0"):
				break
			if(str2=="11064000"):
				time.sleep(120)
				break
			if(str2=="13012000"):
				print Now_time()+"***PASSWORD ERROR***"
				exit(0)
	return str2

def kepp_active_http_post():
	t=0
	while 1:
		str1=active_http_post()
		if (str1!="x"):
			print Now_time()+ encoding(str1)
			str2=str1.split('\"')[3]
			if(str2=="0"):
				time.sleep(120)
				continue
			elif(str2=="1"):
				loginl()
				continue
			else:
				continue

while 1:
	try:
		while 1:
			rn=urllib2.urlopen(testurl)
			cc=rn.geturl()
			if (cc==testurl):
				r=active_http_post()
				print Now_time()+encoding(r)
				if (r!="x"):
					str2=r.split('\"')[3]
					if (str2=="0"):
						break
			loginl()
		
		time.sleep(60)
		kepp_active_http_post()
	except urllib2.HTTPError, e:
		 print Now_time()+str(e.code)
		 print Now_time()+ str(e.reason)
	except urllib2.URLError,e:
		 print Now_time()+ str(e.reason)
