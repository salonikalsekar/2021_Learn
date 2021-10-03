from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict(int)

        for idx, i in enumerate(nums):
            if target - i in temp:
                return [temp[target - i], idx]

            temp[i] = idx
