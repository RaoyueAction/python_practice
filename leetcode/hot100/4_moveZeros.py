class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1
# Example usage:
solution = Solution() 
nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]