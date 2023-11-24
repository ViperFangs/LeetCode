class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(1 ,len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(prices[r] - prices[l], max_profit)
        return max_profit