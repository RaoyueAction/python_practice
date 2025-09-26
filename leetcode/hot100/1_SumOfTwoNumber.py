class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """        
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        """
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []
# Example usage:
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]           