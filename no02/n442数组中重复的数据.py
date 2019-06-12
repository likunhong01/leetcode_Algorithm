#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            else:
                res.append(num)
        return res