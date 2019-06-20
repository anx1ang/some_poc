# -*- coding: utf-8 -*-
import oss2
import json

key =''' 

'''

key = json.loads(key)
key = key['data']
key = dict((k.lower(), v) for k, v in key.iteritems())

print key
print key['endpoint']


endpoint = key['endpoint']
auth = oss2.StsAuth(key['accesskeyid'],key['accesskeysecret'],key['securitytoken'])

'''
先上传
'''

bucket = oss2.Bucket(auth, endpoint, key['bucketname'])
bucket.put_object('test.html', key['bucketname'])

'''列文件
bucket = oss2.Bucket(auth, endpoint, 't3test')
for obj in oss2.ObjectIterator(bucket,delimiter='/'):
	if obj.is_prefix():
		print ('directory:'+obj.key)
	else:
		print('file:'+obj.key)
'''

exist = bucket.object_exists('test.html')
if exist:
	print u'bucket upload success'
else:
	print u'bucket upload fail'
'''
删除
'''
bucket.delete_object('test.html')
exist = bucket.object_exists('test.html')

if exist:
	print u'find test.html,can\'t del'
else:
	print u'del success!'