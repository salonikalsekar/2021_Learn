class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float('inf')
        maxVal = float('-inf')

        for p in prices:
            minVal = min(minVal, p)
            maxVal = max(p - minVal, maxVal)

        return maxVal