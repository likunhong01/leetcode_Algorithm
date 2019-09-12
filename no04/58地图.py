#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

m = int(input())
n = int(input())
arr = []

for i in range(m):
    arr.append([int(j) for j in input().split(' ')])

dp = [[0 for j in range(n)] for i in range(m)]
dp[0][0] = arr[0][0]
for i in range(1, n):
    dp[0][i] = arr[0][i] + dp[0][i-1]
for i in range(1, m):
    dp[i][0] = arr[i][0] + dp[i-1][0]

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i][j-1])

print(dp[m-1][n-1])



# i, j = 0
# result = 0
# while i != m - 1 and j != n - 1:
#     result += arr[i][j]
#     if i + 1 < m and j + 1 < n:
#         if arr[i+1][j] < arr[i][j+1]:
#             i += 1
#             continue
#         else:
#             j += 1
#     elif i + 1 >= m :
#         j += 1
#     elif j + 1 >= n:
#         i += 1

# print(result)