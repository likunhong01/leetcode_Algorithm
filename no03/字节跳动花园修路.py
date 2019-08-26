# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

n = int(input())
dp = [1, 1, 2, 6, 16]
if n < 10:
    print(dp[int(n / 2)])
else:
    for i in range(5, int(n / 2) + 1):
        current = 0
        # counter = 1
        # while counter <= i - 2:
        #     current += 2 * dp[i - counter]
        #     counter += 1

        # 循环i次，
        for x in range(i):
            y = i-1-x
            current += dp[x] * dp[y]
            # print(x, y, current)
        dp.append(current)
    print(dp[-1])

