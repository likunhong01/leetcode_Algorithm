# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

n = int(input())
arr = []

'''
2 2 2 2 
2 2 2 2
2 2 2 2
2 2 2 2'''

for i in range(4):
    s = input().split(' ')
    arr.append([int(i) for i in s])

def clear_up1():
    # 整理arr，去0
    for i in range(3):
        for j in range(4):
            if arr[i][j] != 0:
                for k in range(i, -1, -1):
                    if arr[k][j] == 0:
                        arr[k][j] = arr[k+1][j]
                        arr[k+1][j] = 0

def clear_up2():
    # 整理arr下，去0
    for i in range(3, 0, -1):
        for j in range(4):
            if arr[i][j] != 0:
                for k in range(i, 4):
                    if arr[k][j] == 0:
                        arr[k][j] = arr[k-1][j]
                        arr[k-1][j] = 0

def clear_up3():
    # 整理arr左，去0
    for i in range(3):
        for j in range(4):
            if arr[j][i] != 0:
                for k in range(i, -1, -1):
                    if arr[j][k] == 0:
                        arr[j][k] = arr[j][k+1]
                        arr[j][k+1] = 0


def clear_up4():
    # 整理arr右，去0
    for i in range(3, 0, -1):
        for j in range(4):
            if arr[j][i] != 0:
                for k in range(i, 4):
                    if arr[j][k] == 0:
                        arr[j][k] = arr[j][k-1]
                        arr[j][k-1] = 0


def my_print():
    # 分4行打印arr
    for i in arr:
        print(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + ' ' + str(i[3]))


'''1上，2下，3左，4右'''
if n == 1:
    for i in range(3):
        for j in range(4):
            if arr[i][j] == arr[i+1][j]:
                # 移动
                arr[i][j] += arr[i][j]
                arr[i+1][j] = 0
    clear_up1()
    my_print()

if n == 2:
    for i in range(3, 0, -1):
        for j in range(4):
            if arr[i][j] == arr[i-1][j]:
                # 移动
                arr[i][j] += arr[i][j]
                arr[i-1][j] = 0
    clear_up2()
    my_print()

if n == 3:  # 左
    for i in range(3):
        for j in range(4):
            if arr[j][i] == arr[j][i+1]:
                # 移动
                arr[j][i] += arr[j][i]
                arr[j][i+1] = 0
    clear_up3()
    my_print()

if n == 4:  # 右
    for i in range(3, 0, -1):
        for j in range(4):
            if arr[j][i] == arr[j][i-1]:
                # 移动
                arr[j][i] += arr[j][i]
                arr[j][i-1] = 0
    clear_up4()
    my_print()

