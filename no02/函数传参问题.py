#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

def first(a):
    print(id(a))
    a.append('0')
    print(a)

aa = []
print(id(aa))
first(aa)


def fff(b):
    print(id(b))
    b += 'a'
    print(b)


bb = 'bbb'
print(id(bb))
fff(bb)

# 结论：函数传的都是对象，但对象可能是可变的，也可能是不可变的