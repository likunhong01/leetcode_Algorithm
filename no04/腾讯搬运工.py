# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'
# import time as tm

line1 = [int(i) for i in input().split(' ')]
n = line1[0]
m = line1[1]

box = [int(i) for i in input().split(' ')]
# print(box)


# -------
dp = [0]*n
if box[0] <= m:
    dp[0] = 1
else: dp[0] = int(box[0] / m) if box[0]%m == 0 else 1 + int(box[0] / m)

for i in range(1, n):
    dp[i] = dp[i-1] + 1
    dp[i] += int((box[i] - (m - box[i-1] / m)) / m) if (box[i] - (m - box[i-1] / m)) % m == 0 else int((box[i] - (m - box[i-1] / m)) / m) + 1

print(dp)
print(dp[n-1] + 1)




# --------







'''

workers = [0] * n
workers[0] = m  # 一开始都在0位置
# print(workers)
time = 0
while box:
    # 检查是否搬完
    if max(box) <= 0:
        break

    # 循环一遍，移除现有工人的地方的工人数量的物件
    for i in range(n):
        box[i] = box[i] - workers[i] if box[i] > 0 else 0

    # print(box)

    # 减完后如果是负数代表工人闲置，往前挪
    for i in range(n-1):
        # 加上闲置工人数量，如果是是正数代表还没搬完，工人不够
        workers[i+1] += -box[i] if box[i] < 0 else 0
        workers[i] -= -box[i] if box[i] < 0 else 0
        if box[i] == 0:
            # 吧workers[i]移到i+1上
            workers[i+1] += workers[i]
            workers[i] = 0
    # print(workers)
    # print('---')
    time += 1
    # tm.sleep(2)


        # if workers[i] != 0:  # 说明这个地方有工人，可以搬东西
        #     box[i] = box[i] - workers[i]
            # # 如果工人有多，剩下的工人往前走
            # if i < n:
            #     workers[i + 1] += min(-box[i], 0)
            #     workers[i] -= min(-box[i], 0)
            #     # i前面的工人也往前走
            #     for j in range(i):
            #         workers[j+1] = workers[j]

print(time+1)
'''