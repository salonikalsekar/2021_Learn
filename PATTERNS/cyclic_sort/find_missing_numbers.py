class Solution:
    def missingNumbers(self, nums: List[int]) -> int:

        i = 0
        res = []

        while i < len(nums):
            j = nums[i] - 1

            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                res.append(i + 1)


        return res