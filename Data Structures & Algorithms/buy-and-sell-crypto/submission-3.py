class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = len(prices) - 1
        maxi = 0
        for p in range(len(prices)):
            curr = prices[j] - prices[i]
            maxi = max(curr, maxi)

            if prices[p] < prices[i] and p < j:
                i = p
            if prices[-p - 1] > prices[j] and len(prices) - 1 - p > i:
                j = len(prices) - 1 - p
        return maxi