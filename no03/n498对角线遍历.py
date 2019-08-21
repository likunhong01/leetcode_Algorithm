# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


def findDiagonalOrder(matrix):
    m = len(matrix)
    if m == 0: return []
    n = len(matrix[0])
    if m == 1: return matrix[0]
    if m == 1 and n == 1: return matrix[0]
    if n == 1:
        return [i[0] for i in matrix]

    i = 0
    j = 0
    result = []
    reserve = -1
    while True:
        result.append(matrix[i][j])
        if (i == 0 and j < n - 1) or (i == m - 1 and j < n):
            j += 1
            reserve = -reserve
            result.append(matrix[i][j])
            if i == m - 1 and j == n - 1:
                break
        elif (j == 0 and i < m - 1) or (j == n - 1 and i < m):
            i += 1
            reserve = -reserve
            result.append(matrix[i][j])
            if i == m - 1 and j == n - 1:
                break
        i += 1 * reserve
        j -= 1 * reserve
    return result


arr = [
    [1,2,5],
    [3,4,6]
]

print(findDiagonalOrder(arr))
