from collections import Counter
def deleteAndEarn(nums):
    count = Counter(nums)
    prev = None
    avoid = using = 0
    for k in sorted(count):
        if k - 1 != prev:
            avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
        else:
            avoid, using = max(avoid, using), k * count[k] + avoid
        prev = k
    return max(avoid, using)


print(deleteAndEarn(([4,8,6,12])))