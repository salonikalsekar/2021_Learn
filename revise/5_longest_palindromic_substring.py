class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxVal = float('-inf')
        start = 0
        end = 0
        for i in range(len(s)):
            l = self.check_palindrome(s, i, i)
            r = self.check_palindrome(s, i, i + 1)

            length = max(l, r)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

    def check_palindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i + - 1
