class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            #print(dp)
        return dp[n]
# Example usage:
solution = Solution()
print(solution.fib(10))  # Output: 55
# The above code defines a class Solution with a method fib that calculates the nth Fibonacci number using dynamic programming.   