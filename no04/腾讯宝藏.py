# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

line1 = input().split(' ')
n, m = int(line1[0]), int(line1[1])

# 输入宝箱上的数字和钥匙上的数字
arr1 = input().split(' ')
treasure_boxs = [int(s) for s in arr1]
arr2 = input().split(' ')
keys = [int(s) for s in arr2]

# 统计宝箱上有多少个奇数和偶数
t_ji = 0
t_ou = 0
for num in treasure_boxs:
    if num % 2 == 0:
        t_ou += 1
    else:
        t_ji += 1

# 统计钥匙上有多少个奇数和偶数
k_ji = 0
k_ou = 0
for num in keys:
    if num % 2 == 0:
        k_ou += 1
    else:
        k_ji += 1

result = min(t_ji, k_ou) + min(t_ou, k_ji)
print(result)
