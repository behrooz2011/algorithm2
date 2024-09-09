
"""
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
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104"""
def maxSubArray(nums):
    window = nums[0]
    res = nums[0]
    left = 0
    
    for right in range(1,len(nums)):
        if window < 0 and nums[right] >= 0: # the only situation that matters where we need to change the position of the left pointer
            left = right
            res = max(res, window, window + nums[right], nums[right])
            window = nums[right]
        else:
            window += nums[right]
            res = max(res, window, nums[right])
    return res
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))