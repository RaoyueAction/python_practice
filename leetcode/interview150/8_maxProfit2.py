class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        total_profit = 0
        for i in range(1,n):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        return total_profit
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,4,6]))