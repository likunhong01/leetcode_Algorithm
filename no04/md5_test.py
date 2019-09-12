# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

import hashlib

import hashlib

# 待加密信息
str = 'lasdhgoqasdi2932j3bo2y032lei2k3l'

# 创建md5对象
hl = hashlib.md5()

# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())
print('MD5加密后长度 ：', len(hl.hexdigest()))

arr = [
    {'aaa': 123, 'bbb': 333},
    {'ccc': 456},
    {'aaa': 777, 'bbb': 888}
]
