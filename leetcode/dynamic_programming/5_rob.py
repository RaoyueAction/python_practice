class Solution:
    def rob(self, nums: list[int]) -> int:
        prev1, prev2 = 0, 0

        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        return prev1
    
#example
s = Solution()
print(s.rob([1,2,3,1]))  # Output: 4