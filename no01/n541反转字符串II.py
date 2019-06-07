#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        le = len(s)
        for x in range(int(le / (2 * k)) + 1):
            s = s[0:2*k*x] +s[2*k*x:min(le, 2*k*x+k)][::-1]+s[min(le, 2*k*x+k):]
        return s


s1 = Solution()
print(s1.reverseStr('12345678', 3))