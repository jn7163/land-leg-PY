__author__ = 'mynuolr'
__Email__='mynuolr@foxmail.com'
__Blog__ = 'http://www.renjianfeng.cn'
__Github__ = 'https://github.com/mynuolr/GD-esurfingschoolclient-portal'
__QQGroup__='151078659'
import logging
import urllib2
import time
import json
ISOTIMEFORMAT='%Y-%m-%d %X'
client="0.0.0."             #Your client ip
nasip="0.0.0.0"             #Your nasip
user=""                     #YOUR user
pawssword=""                #PASSWORD
mac="00-00-00-00-00-00"     #MAC ADDRESS
url="http://enet.10000.gd.cn:10001/client/"
login = url + "login"
challenge = url + "challenge"
active="http://enet.10000.gd.cn:8001/hbservice/client/active?"
testurl="http://www.baidu.com/"
dianxin="Eshore!@#"
def getmd5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
def GetTime():
    return  int((time.time()*1000))/1
def log(str):
    log_format = '[%(asctime)s] [INFO] %(message)s'
    logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S %p',filename='protal.log',level=logging.DEBUG)
    logging.debug(str)
def chall_http_post():
        timestr=str(GetTime())
        str1=str(client+nasip+mac+timestr+dianxin)
        md5str=getmd5(str1).upper()
        bb="MD5>>>>>>>>>"+md5str
        print("MD5>>>>>>>>>"+md5str)
        log(bb)
        url=challenge
        values ={"username":user,"clientip":client,"nasip":nasip,"mac":mac,"timestamp":timestr,"authenticator":md5str}
        jdata = json.dumps(values)
        print(values)
        log(values)
        req = urllib2.Request(url, jdata)
        response = urllib2.urlopen(req)
        return response.read()
def getToken(re):
    re = re.split("\",\"")[0]
    re = re.split("\":\"")[-1]
    return re
def Now_time():
    return time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
def login_http_post(token):
        timestr=str(GetTime())
        str1=str(client+nasip+mac+timestr+token+dianxin)
        md5str=getmd5(str1).upper()
        bb="MD5>>>>>>>>>"+md5str
        print("MD5>>>>>>>>>"+md5str)
        log(bb)
        url=login
        values ={"username":user,"password":pawssword,"clientip":client,"nasip":nasip,"mac":mac,"timestamp":timestr,"authenticator":md5str,"iswifi":"1050"}
        jdata = json.dumps(values)
        print(values)
        log(values)
        req = urllib2.Request(url, jdata)
        response = urllib2.urlopen(req)
        return response.read()
def encoding(data):
    types = ['utf-8','gb2312','gbk','iso-8859-1']
    for type in types:
        try:
            return data.decode(type)
        except:
            pass
        return None
def xintiao():
     timestr=str(GetTime())
     str1=str(client+nasip+mac+timestr+dianxin)
     md5str=getmd5(str1).upper()
     bb="MD5>>>>>>>>>"+md5str
     print("MD5>>>>>>>>>"+md5str)
     log(bb)
     url=active+"username="+user+"&clientip="+client+"&nasip="+nasip+"&mac="+mac+"&timestamp="+timestr+"&authenticator="+md5str
     bb="GET "+url
     log(bb)
     print(bb)
     response = urllib2.urlopen(url)
     log(response.read())
     print (response.read())
     return response.read()
def iflogin(str):
    re=str
    re1=re.split('\"')[-6]
    if (re1=="0"):
        return encoding(re.split('\"')[-2])
    return "No Login"
def loginl():
    while 1:
        ls=login_http_post(getToken(chall_http_post()))
        log(ls)
        str2=ls.split('\"')[3]
        if(str2=="0"):
            break
def kepp_xintiao():
    t=0
    while 1:
        str=xintiao()
        time.sleep(60)
        t=t+1
        if (t==5):
            str2=str.split('\"')[-6]
            if (str2 !="0"):
                t=0
                while 1:
                   try:
                     l= urllib2.urlopen(testurl)
                     loginl()
                     break
                   except urllib2.HTTPError, e:
                     print e.code
                     print e.reason
                break
while 1:
    rn=urllib2.urlopen(testurl)
    try:
        if (rn.geturl()!=testurl):
            loginl()
            time.sleep(60)
        kepp_xintiao()
    except urllib2.HTTPError, e:
         print e.code
         print e.reason