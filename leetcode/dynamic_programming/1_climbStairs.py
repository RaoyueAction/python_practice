class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1,2
        for i in range(3, n + 1):
            first, second = second, first + second
        # The second variable holds the number of ways to climb n stairs
        return second
