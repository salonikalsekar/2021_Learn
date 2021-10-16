class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_index = 1
        i = 1

        while i < len(nums):
            if nums[i] != nums[duplicate_index - 1]:
                nums[duplicate_index] = nums[i]
                duplicate_index += 1
            i += 1

        return duplicate_index
