#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

'''
某校在积极推行无人监考制度，但是总有学生是不自觉的，如果将两个很熟的异性朋友放在同一个考场里，
他们就会交流甚至作弊。因此一个考场中不能允许两个很熟的异性朋友存在，学校希望通过搬出一部分学生
的方法来改善这一问题。
但是又因为教室数量有限，因此希望一个教室中容下的学生尽可能多，即需要搬出教室的学生数量尽可能少，
请你输出搬出教室人数最少，且字典序最小的方案。
'''



diyihang = input().split(' ')
n = int(diyihang[0])
m = int(diyihang[1])
dic = {}
guanxitu = [[0] * (n+1) for i in range(n+1)]
# print(guanxitu)
kaochang = [i for i in range(0,n * 2)]
shanchu = []

# 判断考场是否是ok的
def ok():
    for i in range(1, n+1):
        # 遍历男生，只要男生有关系的女生都不在就算考场没问题
        for j in range(1, n+1):
            if guanxitu[i][j] == 1:
                # 看这个女的在不在考场里，在就返回false
                # if j + n in kaochang and i in kaochang:
                #     return False
                return False
    return True

# 把关系图做好
for i in range(m):
    hang = input().split(' ')
    nan = int(hang[0])
    nv = int(hang[1])
    if nan > nv:
        nv, nan = nan, nv
    nv -= n
    # print(nan,nv)
    guanxitu[nan][nv] = 1

# 开始删人
while(not ok()):
    # 贪心法删人，删关系最多的人
    # print(guanxitu)

    # 先算男的关系最多的人
    max_nan = 0
    max_nan_count = 0
    for i in range(1,n+1):
        if i in shanchu:
            continue
        count = 0
        for j in range(1,n+1):
           count += guanxitu[i][j]
        if count > max_nan_count:
            max_nan_count = count
            max_nan = i

    # 女的关系最多的人
    max_nv = 0
    max_nv_count = 0
    for i in range(1,n+1):
        if i+n in shanchu:
            continue
        count = 0
        for j in range(1,n+1):
            count += guanxitu[j][i]
        if count > max_nv_count:
            max_nv_count = count
            max_nv = i

    # 比较男女哪个多
    max_ren = max_nv + n if max_nan_count < max_nv_count else max_nan

    shanchu.append(max_ren)
    # kaochang.remove(max_ren)

    if max_ren <= n: # 是男生
        for k in range(1, n + 1):
            guanxitu[max_ren][k] = 0
    else:
        for k in range(1, n + 1):
            guanxitu[k][max_ren - n] = 0

# print('----')
shanchu.sort()
print(len(shanchu))
s = ''
for i in shanchu:
    s += i + ' '
print(s)