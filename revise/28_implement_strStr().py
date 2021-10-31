class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        if haystack:
            if not needle:
                return 0
            t = haystack.split(needle)
            if len(t[0]) == len(haystack):
                return -1
            else:
                return len(t[0])

        else:
            if needle:
                return -1
            return 0