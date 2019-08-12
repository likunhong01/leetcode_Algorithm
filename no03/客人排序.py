# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

import sys


class keren:
    def __init__(self, renshu, qian):
        self.renshu = renshu
        self.qian = qian

    # def __cmp__(self, other):
    #     if self.qian > other.qian:
    #         return 1
    #     elif self.qian > other.qian:
    #         return -1
    #     else:
    #         return 0

    def __eq__(self, other):
        return self.qian == other.qian

    def __le__(self, other):
        return self.qian < other.qian

    def __gt__(self, other):
        return self.qian > other.qian

    def __str__(self):
        return 'renshu:{},qian:{}'.format(self.renshu, self.qian)


if __name__ == "__main__":
    # 读取每一行
    # line = sys.stdin.readline().strip()
    # # 把每一行的数字分隔后转化成int列表
    # values = list(map(int, line.split()))
    #
    # n = values[0]
    # m = values[1]
    # maxrongna = values[2:2 + n]
    # bc = values[2 + n:]
    # b = [values[i * 2 + 2 + n] for i in range(int(len(bc) / 2))]
    # c = [values[i * 2 + 3 + n] for i in range(int(len(bc) / 2))]
    # bcbc = [keren(b[i], c[i]) for i in range(len(b))]

    n = 2
    m = 5
    maxrongna = [5,6]
    keren1 = keren(1, 10)
    keren2 = keren(2, 18)
    keren3 = keren(5, 60)
    keren4 = keren(3, 60)
    keren5 = keren(7, 110)
    bcbc = [keren1,keren2,keren3,keren4,keren5]

    # 按消费排序，优先安排消费高的
    bcbc = sorted(bcbc,reverse=True)
    for i in bcbc:
        print(i)

    # n要开始减了
    maxvalue = 0
    for i in bcbc:

        lssz = []
        for nn in maxrongna:
            if i.renshu < nn:
                lssz.append(nn)
        if lssz:
            x = min(lssz)
            index = maxrongna.index(x)
            print(x)  # 找到了最接近这波人的桌子
            print(maxrongna)
            for nn in maxrongna:
                if nn == x:
                    maxrongna[index] = 0  # 把这个位置取消
            maxvalue += i.qian

    print(maxvalue)
