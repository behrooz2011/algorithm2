class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeros = {}
        product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeros[i] = i
        if len(zeros) > 1:
            return [0] * len(nums)
        if len(zeros) == 1:
            arr = [0] * len(nums)
            nonZeroKey = list(zeros.keys())[0]
            arr[nonZeroKey] = product
            return arr
        if len(zeros) == 0:
            return [product/x for x in nums]
        