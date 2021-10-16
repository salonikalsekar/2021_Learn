class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            j = nums[i] - 1
            if nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        print(nums)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])

        return res