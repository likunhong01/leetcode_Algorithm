#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        baoshi = {}
        count = 0
        for i in J:
            baoshi[i] = 1
        for i in S:
            if i in baoshi:
                count += 1
        return count

s = Solution()
print(s.numJewelsInStones('aA', 'aaAAbdds'))