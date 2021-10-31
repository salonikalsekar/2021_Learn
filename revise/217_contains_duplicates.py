class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        non_dup = 1
        i = 1

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                return True

            i += 1

        return False