class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        startIdx = 0
        size = float('inf')
        window_total = 0

        for endIdx in range(len(nums)):

            window_total += nums[endIdx]

            if window_total >= target:

                while window_total >= target:
                    size = min(size, (endIdx - startIdx) + 1)
                    window_total -= nums[startIdx]
                    startIdx += 1

        if size != float('inf'):
            return size
        else:
            return 0