#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

n = int(input())
s = input().split(' ')
ss = [int(i) for i in s]

dp = [1] * n
for i in range(1,n):
    max_ = 0
    for j in range(i):
        if ss[i] > ss[j]:
            max_ = max(max_, dp[j])
    if max_:
        dp[i] = max_ + 1

print(max(dp))

