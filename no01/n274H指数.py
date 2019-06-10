#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

class Solution:
    def hIndex(self, citations):
        citations.sort()
        leng = len(citations)
        for i in range(leng, -1,-1):
            h = citations[i - 1]
            # 每个值循环，从最大开始
            # 统计数组里符合条件的个数
            count = 0
            count2 = 0
            for ci in citations:
                if ci >= h:
                    count += 1
                if ci < h:
                    count2 += 1
            if count <= h and count2 == i - 1:
                return h
        return 0

    def h(self, citations):
        citations.sort()
        l = len(citations)
        for index, ci in enumerate(citations):
            h = l - index
            if ci >= h:
                return h
        return 0

s = Solution()
print(s.h([3,0,6,1,5]))
print(s.hIndex([3,0,6,1,5]))