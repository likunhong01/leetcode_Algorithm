# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

arr = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

for i in range(max(len(arr[0]))):
    n = arr[i][0] if arr[i][0] else 0
    n = arr[i][len(arr[0]) - 1] if arr[i][len(arr[0]) - 1] else 0
    n = arr[0][i] if arr[0][i] else 0
    n = arr[len(arr) - 1][i] if arr[len(arr) - 1][i] else 0
