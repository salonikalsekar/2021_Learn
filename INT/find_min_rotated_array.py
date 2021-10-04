class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[j]:
            return nums[0]

        while i < j:

            mid = (i + j) // 2

            if nums[mid] < nums[j]:
                j = mid

            else:
                i = mid + 1

        return nums[i]
