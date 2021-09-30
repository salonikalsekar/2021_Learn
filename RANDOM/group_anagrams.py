from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = defaultdict(list)

        for i in strs:
            key = ''.join(sorted(i))
            t[key].append(i)

        return t.values()