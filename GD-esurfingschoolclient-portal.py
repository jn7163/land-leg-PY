__author__ = 'mynuolr'
__Email__='mynuolr@foxmail.com'
__Blog__ = 'http://www.renjianfeng.cn'
__Github__ = 'https://github.com/mynuolr/GD-esurfingschoolclient-portal'
__QQGroup__='151078659'

import urllib2
import time
import json
ISOTIMEFORMAT='%Y-%m-%d %X'
client=“0.0.0.0”                #client ip
nasip=“0.0.0.0”                 #net auth ip
user=“user“                     #user
password=“password”                      #password
mac=“FF-FF-FF-FF-FF-FF“               #mac address eg.FF-FF-FF-FF-FF-FF
wifi="1050"			#LOGIN
url="http://enet.10000.gd.cn:10001/client/"
login = url + "login"
challenge = url + "challenge"
active="http://enet.10000.gd.cn:8001/hbservice/client/active?"
dianxin="Eshore!@#"
testurl="http://10000.gd.cn"
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
def chall_http_post():
        timestr=str(GetTime())
        str1=str(client+nasip+mac+timestr+dianxin)
        md5str=getmd5(str1).upper()
        print Now_time()+"MD5>>>>>>>>>"+md5str
        url=challenge
        values ={"username":user,"clientip":client,"nasip":nasip,"mac":mac,"timestamp":timestr,"authenticator":md5str}
        jdata = json.dumps(values)
        print Now_time()+ str(values)
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
        print Now_time()+re,
        re = re.split("\",\"")[0]
        re = re.split("\":\"")[-1]
        return re
    else:
        return "x"
def Now_time():
     t1=time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
     str="[ "+t1+" ]\t"
     return str
def login_http_post(token):
        timestr=str(GetTime())
        str1=str(client+nasip+mac+timestr+token+dianxin)
        md5str=getmd5(str1).upper()
        print Now_time()+"MD5>>>>>>>>>"+md5str
        url=login
        values ={"username":user,"password":password,"clientip":client,"nasip":nasip,"mac":mac,"timestamp":timestr,"authenticator":md5str,"iswifi":wifi}
        jdata = json.dumps(values)
        print Now_time()+str(values)
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
def xintiao():
     timestr=str(GetTime())
     str1=str(client+nasip+mac+timestr+dianxin)
     md5str=getmd5(str1).upper()
     print Now_time()+"MD5>>>>>>>>>"+md5str
     url=active+"username="+user+"&clientip="+client+"&nasip="+nasip+"&mac="+mac+"&timestamp="+timestr+"&authenticator="+md5str
     req = urllib2.Request(url)
     print Now_time()+"GET "+url
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
        ls=login_http_post(getToken(chall_http_post()))
        print Now_time()+ls,
        if (ls !="x"):
            str2=ls.split('\"')[3]
            if(str2=="0"):
               break
    return str2
def kepp_xintiao():
    t=0
    while 1:
        str1=xintiao()
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
        while 1 :
            rn=urllib2.urlopen(testurl)
            cc=rn .geturl()
            if (cc==testurl):
                r=xintiao()
                print Now_time()+encoding(r)
                if (r!="x"):
                    str2=r.split('\"')[3]
                    if (str2=="0"):
                        break
            loginl()
            
        time.sleep(60)
        kepp_xintiao()
    except urllib2.HTTPError, e:
         print Now_time()+str(e.code)
         print Now_time()+ str(e.reason)
    except urllib2.URLError,e:
         print Now_time()+ str(e.reason)
