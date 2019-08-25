#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'



n = int(input())

relation = []

for i in range(n):
    s = input().split(' ')
    relation.append([int(i) for i in s])

inputed = []
count = 0

def digui(i, end):
    for k in range(i+1, n):
        if relation[i][k] >= 3:
            inputed.append(k)
            # tmp = relation[i][k]
            relation[i][k] = -1
            digui(k, end)
            # relation[i][k] = tmp
    # if i == end:
    #     return 1


for i in range(n):
    if i in inputed:
        continue
    count += 1
    inputed.append(i)
    for j in range(i + 1, n):
        if relation[i][j] >= 3:
            # 说明有关系，递归去查找和这个人所有的豆油瓶
            inputed.append(j)
            relation[i][j] = -1
            digui(j, j)


print(count)
