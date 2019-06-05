#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums or len(nums) == 1 :
            return nums
        leng = len(nums)
        nums.sort()
        dp = [[i] for i in nums]
        for i in range(1,leng):
            for j in range(i, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[j] + [nums[i]], dp[i], key=len)
                    dp[i] = list(set(dp[i]))
        return max(dp, key=len)

s = Solution()
rs = s.largestDivisibleSubset([1,2,3])
print(rs)