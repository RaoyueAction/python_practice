class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_num = max(nums)
        points = [0] * (max_num + 1)

        for num in nums:
            points[num] += num

        dp = [0] * (max_num + 1)
        dp[1] = points[1]

        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

        return dp[max_num]
    
# Example
s = Solution() 
print(s.deleteAndEarn([3, 4, 2]))  # Output: 6
print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))  # Output: 9