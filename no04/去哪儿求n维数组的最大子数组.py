#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

n = int(input())
line = [int(i) for i in input().split(' ')]
arr = [line[i*n:i*n+n] for i in range(n)]

result = 0
for i in arr:
    result = max(sum(i), result)

for i in range(n):
    t = 0
    for j in range(n):
        t += arr[j][i]
    result = max(t, result)

print(result)
