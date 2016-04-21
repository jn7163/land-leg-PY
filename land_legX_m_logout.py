import urllib2
import time
import json
print 'Powered by XenK0u http://henbukexue.science'
print '----------------LOGOUT----------------'
print
clientip="马赛克"#your LAN IP
user="马赛克"#your account
password="马赛克"#your password
mac="马赛克"#your MAC address(FF-FF-FF-FF-FF-FF)
ISOTIMEFORMAT='%Y-%m-%d %X'
nasip="219.128.230.1"
wifi="4060"#1050
secret="Eshore!@#"
ua='Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'

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

def Now_time():
	t1=time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
	str="["+t1+"] "
	return str

def logout_http_post():
	timestr=str(GetTime())
	str1=str(clientip+nasip+mac+timestr+secret)
	md5str=getmd5(str1).upper()
	print Now_time()+"logout..."
	url="http://enet.10000.gd.cn:10001/client/logout";
	values ={"clientip":clientip,"nasip":nasip,"mac":mac,"timestamp":timestr,"authenticator":md5str}
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

ls=logout_http_post()
print Now_time()+encoding(ls)
time.sleep(5)
