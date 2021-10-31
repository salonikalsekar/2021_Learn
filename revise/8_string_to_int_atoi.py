class Solution:
    def myAtoi(self, str: str) -> int:

        num = ""
        str = str.lstrip(" ")

        if not str:
            return 0

        if str[0] in ["-", "+"]:
            num = str[0]
            str = str[1:]

        for ch in str:
            if ch.isdigit():
                num += ch
            else:
                break

        try:
            num = int(num)
            if num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif num < -2 ** 31:
                return -2 ** 31
            return num

        except ValueError:
            return 0

