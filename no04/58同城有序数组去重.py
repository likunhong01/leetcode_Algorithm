#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

arr = [int(i) for i in input().split(',')]
d = {}
for a in arr:
    d[a] = 1
print(len(d))