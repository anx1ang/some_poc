# -*- coding: utf-8 -*-
import oss2

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('KrrJurCq1W17J3ys', 'T7BpTRu13rU17eT6G3fHywDmlJSxQc')
# Endpoint以杭州为例，其它Region请按实际情况填写。
#
service = oss2.Service(auth, 'http://oss-cn-hangzhou.aliyuncs.com')
print([b.name for b in oss2.BucketIterator(service)])
# 设置存储空间为私有读写权限。
#bucket.create_bucket(oss2.models.BUCKET_ACL_PRIVATE)