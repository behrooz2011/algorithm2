""" A subsequence is an array that can be derived from another array by deleting some or 
no elements without changing the order of the remaining elements"""

"""
300. Longest Increasing Subsequence
Solved
Medium
Topics
Companies
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###### f(n) = 2*f(n-1) + 1 #####
        # maxRes = 1
        # # nums = [1,10,3,9]
        # sub = [[nums[0]]]
        # for i in range(1,len(nums)):
        #     for j in range(len(sub)):
        #         if nums[i] > sub[j][-1]:
        #             temp = sub[j] + [nums[i]]
        #             sub.append(temp)
        #             maxRes = max(maxRes, len(temp))
        #     sub.append([nums[i]])
        # # print(sub)
        # return maxRes  # Time Exceeded!#


        ##### solution 2 ##########
        if not nums:
            return 0
        
        dp = [1] * len(nums)  # dp[i] will hold the length of the LIS ending at index i
        max_length = 1  # At least one element means LIS of at least length 1
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_length = max(max_length, dp[i])
        
        return max_length