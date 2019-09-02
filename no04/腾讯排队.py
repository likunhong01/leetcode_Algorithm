# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

import numpy as np

# a = np.array([[2, 7, 4, 2],
#               [35, 9, 1, 5],
#               [22, 12, 3, 2]])

n = int(input())
arr = [[0, 0] for i in range(n)]
for i in range(n):
    s = input().split(' ')
    arr[i][0] = int(s[0])
    arr[i][1] = int(s[1])

# sorted(arr, key=lambda x: (x[0]))
a = np.array(arr)

# print('按第一列顺序排序:')
# arr_s = a[np.lexsort(a[:, ::-1].T)]

# 先按第一列升序，再按第二列降序
arr_s = a[np.lexsort([a[:, 1], -1 * a[:, 0]]), :]
# print(arr_s)


# dissatisfied[j] = arr[j][0] * (j-1) + arr[j][1] * (n-j)
# dissatisfied = [0] * n
result = 0
for j in range(n):
    # dissatisfied[j] = arr_s[j][0] * j + arr_s[j][1] * (n - j - 1)
    # result += dissatisfied[j]
    # print(dissatisfied[j])
    result += arr_s[j][0] * j + arr_s[j][1] * (n - j - 1)
print(result)

# -------------------
n = int(input())
arr = [[0, 0] for i in range(n)]
for i in range(n):
    s = input().split(' ')
    arr[i][0] = int(s[0])
    arr[i][1] = int(s[1])

# 先按第一列升序，再按第二列降序
arr_s = sorted(arr, key=lambda x: (x[1], -x[0]))

result = 0
for j in range(n):
    result += arr_s[j][0] * j + arr_s[j][1] * (n - j - 1)
print(result)
