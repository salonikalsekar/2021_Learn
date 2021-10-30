class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverseS(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]

                i += 1
                j -= 1

        start = 0
        end = 0
        while end < len(s):
            if s[end] == " ":
                reverseS(start, end - 1)
                start = end + 1
            end += 1

        reverseS(start, end - 1)
        reverseS(0, len(s) - 1)
