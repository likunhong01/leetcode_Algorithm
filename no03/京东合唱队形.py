#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


n = int(input())
arr = [int(i) for i in input().split(' ')]
# min_index = 0
# count = 0
# while(min_index < n):
#     min_num = arr[min_index]
#     for i in range(min_index, n):
#         val = arr[i]
#         if val < min_num:
#             min_num = val
#             min_index = arr.index(val)
#     min_index += 1
#     # print(min_index)
#     count += 1
# print(count)

arr_copy = [i for i in arr]
arr.sort()
count = 0
maxi = 0
for i in arr:
    index = arr_copy.index(i)
    if index >= maxi:
        count += 1
        maxi = index
print(count)

# while True:
#     for index, val in enumerate(arr):
#         if val < min_num:
#             min_num = val
#             min_index = index
#     count += 1

