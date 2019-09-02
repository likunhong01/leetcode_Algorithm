# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

# 5
# 7 2 4 6 5

n = int(input())
arr = [int(i) for i in input().split(' ')]

def get_max_grade(array):
    if len(array) == 0:
        return 0
    if len(array) <= 1:
        return array[0] * array[0]
    min_index = 0
    min_value = array[0]
    for index, i in enumerate(array):
        if i < min_value:
            min_index = index
            min_value = i

    return max(get_max_grade(array[0:min_index]),
               get_max_grade(array[min_index + 1:]),
               min_value * sum(array))

print(get_max_grade(arr))