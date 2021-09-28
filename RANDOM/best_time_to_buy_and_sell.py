class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float('inf')
        maxProfit = float('-inf')

        for i in prices:
            minVal = min(minVal, i)
            maxProfit = max(maxProfit, i - minVal)

        return maxProfit