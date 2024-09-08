class Solution(object):
    def threeSum(self, nums):
        """On3 and On2
        """
        # nums.sort()  # Sort the array to handle duplicates easily
        # result = set()  # Use a set to avoid duplicate triplets
        
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         # Calculate the required third number
        #         required = -(nums[i] + nums[j])
        #         # Check if the required number exists in the remaining part of the array
        #         if required in nums[j + 1:]:
        #             # Add the triplet to the result set
        #             triplet = tuple(sorted((nums[i], nums[j], required)))
        #             result.add(triplet)
        
        # return [list(triplet) for triplet in result]  # Convert set of tuples back to 


        ####################### O(N2)#########################
        nums.sort()  # Step 1: Sort the array
        result = set()  # Use a set to avoid duplicate triplets
        
        for i in range(len(nums) - 2):  # Fix the first number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number //not necessary
                continue
            
            seen = set()  # To track the second number
            for j in range(i + 1, len(nums)):  # Iterate through the rest of the array
                required = -nums[i] - nums[j]  # Calculate the required third number
                
                if required in seen:  # Check if the required number has been seen
                    triplet = (nums[i], nums[j], required)
                    result.add(tuple(sorted(triplet)))  # Add the triplet to the result set
                
                seen.add(nums[j])  # Add the current number to the seen set
                
        return [list(triplet) for triplet in result]  # Convert set of tuples back to list of lists

        # # Example usage:
        # print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
        # print(three_sum([0, 1, 1]))  # Output: []
        # print(three_sum([0, 0, 0]))  # Output: [[0, 0, 0]]