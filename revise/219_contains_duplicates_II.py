from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = defaultdict(list)

        for idx, v in enumerate(nums):
            if v not in h:
                h[v].append(idx)

            else:
                for i in h[v]:
                    if idx - i <= k:
                        return True
                h[v].append(idx)

        return False