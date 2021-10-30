class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in d:
                if stack:
                    top = stack.pop()
                    if top != d[ch]:
                        return False
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        if not stack:
            return True
        else:
            return False