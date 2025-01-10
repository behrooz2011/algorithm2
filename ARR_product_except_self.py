"""
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."""

def kk(nums):
        res = [0] * len(nums)
        order = {"product": 1, "zeross" :[]}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                order["zeross"].append(i)
            else:
                order["product"] = order["product"]*nums[i]
        print(order)
        if len(order["zeross"]) == 1:
            print("hello")
            res[order["zeross"][0]] = order["product"]
            return res
        if len(order["zeross"]) > 1:
            return res
        if len(order["zeross"]) == 0:
            for i in range(len(res)):
                if i != order["zeross"]:
                    res[i] = order["product"] / nums[i]
                else:
                    res[i] = 0
            return res