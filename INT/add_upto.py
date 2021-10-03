
def sumDigits(n):
    result = 0
    while (n > 0):
        lastDigit = n % 10
        result += lastDigit
        n = int(n / 10)
    return result


def addDigits(n):
    i = 0
    while (n >= 20):
        n = sumDigits(n)
    return n



print(addsuptoK(20, 5))
print(addsuptoK(20, 15))