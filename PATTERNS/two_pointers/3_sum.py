class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def searchTriplets(triplets, i, target):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                curr_sum = nums[left] + nums[right]

                if curr_sum == target:
                    triplets.append([nums[left], nums[right], -target])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_sum > target:
                    right -= 1
                else:
                    left += 1

        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            searchTriplets(triplets, i, -nums[i])

        return triplets
