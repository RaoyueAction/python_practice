class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # The first k elements of nums are now the elements that are not equal to val
        return k
        # Optionally, you can truncate the list to the new length
        # nums[:] = nums[:k]  # Uncomment if you want to truncate the list 
        # This line is not necessary for the problem, but it can be used to visualize the result