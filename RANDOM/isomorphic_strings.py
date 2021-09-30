from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = set()

        temp = {}

        for i in range(len(s)):
            if s[i] not in temp and t[i] not in seen:
                temp[s[i]] = t[i]

                seen.add(t[i])

            elif s[i] not in temp and t[i] in seen:
                return False

            elif temp[s[i]] != t[i]:
                return False

        return True