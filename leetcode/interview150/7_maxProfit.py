class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))  # Output: 5
    print(s.maxProfit([7,6,4,3,1]))    # Output: 0