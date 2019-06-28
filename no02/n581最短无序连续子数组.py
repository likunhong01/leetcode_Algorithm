#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

class Solution:
    def findUnsortedSubarray(self, nums):
        # diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        # return len(diff) and max(diff) - min(diff) + 1
        s_nums = sorted(nums)
        leng = len(nums)
        index_l = 0
        index_r = leng - 1
        while index_l < leng:
            if nums[index_l] == s_nums[index_l]:
                index_l += 1
            else:
                break
        while index_r >= 0:
            if nums[index_r] == s_nums[index_r]:
                index_r -= 1
            else:
                break
        return max(0, index_r - index_l + 1)

s = Solution()
print(s.findUnsortedSubarray([1,2,5,6]))

