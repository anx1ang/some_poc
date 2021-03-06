# -*- coding: utf-8 -*-
import oss2
import json

key =''' 
{"code":0,"msg":"访问成功","domain":"http://mars.sharedaka.com","data":{"securityToken":"CAIS8wF1q6Ft5B2yfSjIr5fBD+DynIpMhaGxe3X7sXkdNMRtgb/fhzz2IHBNdXNvCesYvvUxmmFY6PcZlqNvRoRZAFDDbsZ2tn/eW6AzJtivgde8yJBZor/HcDHhJnyW9cvWZPqDP7G5U/yxalfCuzZuyL/hD1uLVECkNpv74vwOLK5gPG+CYCFBGc1dKyZ7tcYeLgGxD/u2NQPwiWeiZygB+CgE0DkutfvnmJHGt0uF3AKmk9V4/dqhfsKWCOB3J4p6XtuP2+h7S7HMyiY46WIRpP4n1vMUommX74/DUgkPsk6cUfDZ+9EqMg51a68qxnDsdXYkW5cagAGdjoZfulBHQ2emNEx8t/LZUbNDRDLy9iFIhuIhiO9X149+oc7VoZGn5M47i/8CxlVkBibVj/AyHGMBbcpsz7OYWz4OnLq/Fu8G8Ecz0CLp+FBFQ7/xmQeOUeEFU0LfLcvkJszDt0fYU3ZdJdGu+aiPczvYIfCOH8fS+k3d30HV9g==","accessKeyId":"STS.NTtDZFqUm2cZySJUyH8KAnzte","accessKeySecret":"4gMcv7qsRTZvhHt1GxaK8htcDpn9ZvuWSGEwvPVrba33","expiration":"2020-01-15T13:42:12Z"},"success":true}
'''
key = json.loads(key)['data']
key = dict((k.lower(), v) for k, v in key.iteritems())

print key
#print key['endpoint']


endpoint = 'oss-cn-qingdao.aliyuncs.com'
auth = oss2.StsAuth(key['accesskeyid'],key['accesskeysecret'],key['securitytoken'])

'''
先上传
'''
service = oss2.Service(auth, 'oss-cn-beijing.aliyuncs.com')
print([b.name for b in oss2.BucketIterator(service)])
bucket = oss2.Bucket(auth, endpoint, 'xiaodaka')
bucket.put_object('test.html', 'xiaodaka')

'''列文件'''
bucket = oss2.Bucket(auth, endpoint, 'sharedaka')
for obj in oss2.ObjectIterator(bucket,delimiter='/'):
	if obj.is_prefix():
		print ('directory:'+obj.key)
	else:
		print('file:'+obj.key)


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