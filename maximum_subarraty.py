"""53. Maximum Subarray
Solved
Medium
Topics
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23."""
def maxSubArray(nums):
    # negative = [x for x in nums if x < 0]
    # if len(negative) == len(nums) :
    #     return [max(nums)]
    # sum = 0
    # newSum = 0
    # temp = 0

    # left = 0
    # right = 0

    # newLeft = 0
    # newRight = 0

    # for i in range(len(nums)):
    #     temp += nums[i]
    #     if temp < 0:
    #         left += 1
    #         right += 2
    #         temp = 0
    #     else:
    #         newSum += temp
    #         if newSum > sum:
    #             sum = newSum
    #             left = i
    #             right = i+1





