#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

matrix = [
   [1, 5, 6],
   [3, 7, 10],
   [8, 9, 12]
]

def kthSmallest(matrix, k):
    minn = matrix[0][0]
    maxx = matrix[-1][-1]
    # print(minn, maxx)
    while minn < maxx:
        mid = minn + int((maxx - minn) / 2)
        count = 0
        j = len(matrix[0]) - 1
        for i in range(len(matrix[0])):
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += j + 1
        if count < k:
            minn = mid + 1
        else:
            maxx = mid
    return minn
    pass

print(kthSmallest(matrix, 2))