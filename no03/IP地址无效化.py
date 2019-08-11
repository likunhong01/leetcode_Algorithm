#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


def defangIPaddr(address: str) -> str:
    return address.replace('.', '[.]')


print(defangIPaddr('123.2'))

