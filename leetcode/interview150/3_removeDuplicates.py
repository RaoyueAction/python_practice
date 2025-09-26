class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[write_index - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
# Example usage:
solution = Solution()     
nums = [1, 1, 2, 2, 3, 3]
length = solution.removeDuplicates(nums)    
print(length)  # Output: 3
print(nums[:length])  # Output: [1, 2 ，3]