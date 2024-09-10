"""
152. Maximum Product Subarray
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
https://www.youtube.com/watch?v=lXVy6YWFcRM&t=621s
"""
def maxProductSubarray(nums):
    """
    Finds the maximum product of a subarray in the given integer array.

    Args:
        nums: The input integer array.

    Returns:
        The maximum product of a subarray.
    """

    # Initialize variables to keep track of the maximum and minimum products so far
    max_product = nums[0]
    min_product = nums[0]

    # Initialize variables to store the results
    result = nums[0]

    # Iterate through the array, starting from the second element
    for i in range(1, len(nums)):
        # Update the maximum and minimum products based on the current element
        temp_max = max(nums[i], max_product * nums[i], min_product * nums[i])
        min_product = min(nums[i], max_product * nums[i], min_product * nums[i])
        max_product = temp_max

        # Update the result if the current maximum product is greater
        result = max(result, max_product)

    return result

# Example usage:
nums = [2, 3, -2, 4]
print(maxProductSubarray(nums))  # Output: 6