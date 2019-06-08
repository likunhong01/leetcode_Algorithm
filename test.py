#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

print([123,456] + ['aaa'])

print('12345678'[0:2])

print('123'[::-1])

s1 = '12345'
s1 = s1[0:2][::-1] + s1[2:]
print(s1)

print('.' == '.')

import queue
q1 = queue.Queue()
q1.put(1)
q1.put(None)
while not q1.empty():
    print(q1.get())