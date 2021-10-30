from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #          startIdx = 0
        #         endIdx = len(nums) - 1

        #         while startIdx < endIdx:
        #             if nums[startIdx] + nums[endIdx] == target:
        #                 return [startIdx, endIdx]
        #             elif nums[startIdx] + nums[endIdx] < target:
        #                 startIdx += 1
        #             else:
        #                 endIdx -= 1

        #         return [-1, -1]

        temp = defaultdict(int)
        for idx, v in enumerate(nums):

            if target - v in temp:
                return [idx, temp[target - v]]
            else:
                temp[v] = idx

        return [-1, -1]

