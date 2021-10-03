def evenSubarray(nums, k):
    if not nums:
        return []

    size = len(nums)
    nums_str = ''.join([str(x) for x in nums])
    sset = set()
    for i in range(size):
        odds = 0

        for j in range(i, size):
            if nums[j] % 2 == 1:
                odds += 1

            if odds <= k and nums_str[i:j + 1] not in sset:
                sset.add(nums_str[i:j + 1])
    return len(sset)

print(evenSubarray([1,2,3,4], 1))
print(evenSubarray([2,1,2,1,3], 2))