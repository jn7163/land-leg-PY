__author__ = 'mynuolr'
# -*- coding: utf-8 -*-
import time
import uuid
import urllib2

import hashlib
import json
url="http://enet.10000.gd.cn:10001/client/"
login = url + "login"
challenge = url + "challenge"
logout=url+"logout"
active="http://enet.10000.gd.cn:8001/hbservice/client/active"
testurl="http://10000.gd.cn/"
macadd="1C-3E-84-EB-41-D7"
dianxin="Eshore!@#"
def getIp():
    ip_list=[]
    burl=urllib2.urlopen(testurl).geturl()
    values = burl.split('?')[-1]
    for key_value in values.split('&'):
        ip_list.extend( key_value.split('='))
        print ip_list
    print burl
    return ip_list
def time1():
    t=int((time.time()*1000))
    print t
    return t
def getmac():
    mac= uuid.UUID( int=(uuid.getnode())).hex[-12:]
    j=0
    str=""
    print mac
    for i in mac:
        j += 2
        if ((j/2)<=5):
                str=str+mac[j-2:j]+"-"

        if (j==12):
                str=str+mac[j-2:j]

    return macadd

if (urllib2.urlopen(testurl).geturl()==testurl):
    print("login secc")
    exit()
user=raw_input("imput user:")
password = raw_input("input password:")
ip=getIp()
cip=ip[3]
nip=ip[1]

def getMd5(str):
    m = hashlib.md5().update(str)
    return m.hexdigest().upper()

unixTime=str(time1())
resp = http_post(0)
print resp








