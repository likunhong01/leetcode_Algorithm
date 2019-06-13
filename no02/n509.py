#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


def fib(N):
    f = [0 * N]
    f[0] = f[1] = 1
    for i in range(3, N):
        f[i] = f[i - 1] + f[i - 2]
    return f[N-1]



print(fib(4))