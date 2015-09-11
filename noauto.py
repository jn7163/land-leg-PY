__author__ = 'mynuolr'
import logging
import urllib2
import time
import json
ISOTIMEFORMAT='%Y-%m-%d %X'
dianxin="Eshore!@#"
client=“0.0.0.0” #client ip
nasip=“0.0.0.0” #nas ip
user=""
pawssword=""
mac=“00-00-00-00-00-00” #mac adder
url="http://enet.10000.gd.cn:10001/client/"
login = url + "login"
challenge = url + "challenge"
active="http://enet.10000.gd.cn:8001/hbservice/client/active?"
testurl="http://10000.gd.cn/"
def getmd5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
def GetTime():
    return  int((time.time()*1000))/1
def log(str):
    log_format = '%(filename)s [%(asctime)s] [NetWork] %(message)s'
    logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S %p',filename='protal.log',level=logging.DEBUG)
    logging.debug(str)
def chall_http_post():
        timestr=str(GetTime())
        str1=str(client+nasip+mac+timestr+dianxin)
        print str1
        md5str=getmd5(str1).upper()
        print(md5str)
        url=challenge
        values ={"username":user,"clientip":client,"nasip":nasip,"mac":mac,"timestamp":timestr,"authenticator":md5str}
        jdata = json.dumps(values)
        print(values)
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
        print str1
        md5str=getmd5(str1).upper()
        print(md5str)
        url=login
        values ={"username":user,"password":pawssword,"clientip":client,"nasip":nasip,"mac":mac,"timestamp":timestr,"authenticator":md5str,"iswifi":"1050"}
        jdata = json.dumps(values)
        print(values)
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
     print str1
     md5str=getmd5(str1).upper()
     print(md5str)
     url=active+"username="+user+"&clientip="+client+"&nasip="+nasip+"&mac="+mac+"&timestamp="+timestr+"&authenticator="+md5str
     response = urllib2.urlopen(url)
     return response.read()
def iflogin(str):
    re=str
    re1=re.split('\"')[-6]
    if (re1=="0"):
        return encoding(re.split('\"')[-2])
    return "No Login"
def loginl():
    login_http_post(getToken(chall_http_post()))
def kepp_xintiao():
    t=0

    while 1:
        str=xintiao()
        time.sleep(60)
        t=+1
        if (t==5):
            str=iflogin(str)
            if (str !="0"):
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
rn=None
while 1:
    rn=urllib2.urlopen(testurl)
    try:
        l= urllib2.urlopen(testurl)
        if (rn.geturl()==testurl):
            t=iflogin(xintiao())
            if(t!="0"):
                    loginl()
            kepp_xintiao()
        break
    except urllib2.HTTPError, e:

         print e.code
         print e.reason









