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
                    return False
            if ch in d.values():
                stack.append(ch)

        if stack:
            return False
        else:
            return True