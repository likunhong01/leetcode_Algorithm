#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

bg = [1] * n

if n >= 2:
    if arr[1] > arr[0]:
        bg[1] = bg[0] + 1
    else:
        bg[0] = bg[1] + 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        bg[i] = bg[i-1] + 1
    elif arr[i] < arr[i-1]:
        bg[i-1] = max(bg[i] + 1, bg[i-1])
    else:
        bg[i] = bg[i-1]

print(sum(bg))