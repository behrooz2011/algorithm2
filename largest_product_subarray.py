

"""152. Maximum Product Subarray
Solved
Medium
Topics
Companies
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."""
# def maxProduct(arr):
#     product = 1
#     firstProduct =[]
#     result = float('-inf')
#     neg = [x for x in arr if x <= 0]
#     if len(neg) == len(arr):
#         return max(arr)

#     for i in range(len(arr)):
#         if arr[i] != 0:
#             product *= arr[i]
#             if arr[i] < 0:
#                 firstProduct.append(product)
#             result = max(result, product, int(product/firstProduct[0]) if len(firstProduct) != 0 else product,int(product/arr[i]) if arr[i] !=0 and i != 0 else product, arr[i])
#         else:
#             # result = max(maxProduct(arr[:i]), arr[i])
#             result = max(result, arr[i])

#     return result

# # def maxProduct(nums):
#     if not nums:
#         return 0

#     max_so_far = nums[0]
#     min_so_far = nums[0]
#     result = max_so_far

#     for i in range(1, len(nums)):
#         curr = nums[i]
#         print("curr:",curr)
#         temp_max = max(curr, max_so_far * curr, min_so_far * curr)
#         print("temp_max: ",temp_max)
#         min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
#         print("min_so_far: ",min_so_far)

#         max_so_far = temp_max
#         print("max_so_far:",max_so_far)

#         result = max(max_so_far, result)


#     return result
# print(maxProduct([2, 3, -2, 4, 2]))
# print(maxProduct([-2,-3]))
# print(maxProduct([-2,0]))
# print(maxProduct([-2,0,-1]))
# print(maxProduct([2, 3, -2, 4, 2,-1, -5, 1000]))
# print(maxProduct([1,2,3,5,3]))
# print(maxProduct([-3,-1,-1]))