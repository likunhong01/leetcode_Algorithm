#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

# 1 2
# 3 0 1 2
# 2 1 3


line1 = input().split(' ')
k = int(line1[0])
n = int(line1[1])

arr = [[] for i in range(1000000)]

result = 0

for i in range(n):
    line = input().split(' ')
    number = int(line[0])
    now_node = int(line[1])
    tmp_arr = []
    for j in range(2, number+1):
        tmp_arr.append(int(line[j]))
    if i > 0:
        if i in arr[i-1]:
            pass
    result += int((number-1) / k) + 1
    arr[now_node] = tmp_arr

# def get_res(node):
#     if arr[node] is None:
#         return 0
#     else:
#         # if int((len(arr[node])-1) / k) + 1
#         return max([get_res(i) for i in arr[node]]) + int((len(arr[node])-1) / k) + 1
#
# print(get_res(0))

