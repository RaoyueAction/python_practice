class Solution:
    def removeDuplicates(self, nums:list[int] ) -> int:
        if not nums:
            return 0

        write_index = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index
# Example usage:
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
length = solution.removeDuplicates(nums)
print(length)  # Output: 5
print(nums[:length])  # Output: [1, 1, 2, 2, 3]



