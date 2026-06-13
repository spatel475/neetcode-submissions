class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                curr = prices[r] - prices[l]
                profit = max(profit, curr)
            else:
                l = r
            r += 1

        return profit
