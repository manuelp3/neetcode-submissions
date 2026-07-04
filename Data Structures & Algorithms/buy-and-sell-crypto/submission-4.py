class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1
        profit = 0

        while (end < len(prices)):
            diff = prices[end] - prices[start]
            profit = max(profit, diff)

            if (prices[end] < prices[start]):
                start = end
            end += 1
        return profit