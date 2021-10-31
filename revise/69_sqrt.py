class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        return self.sq(low, high, x)

    def sq(self, low, high, x):

        mid = (low + high) // 2

        if low <= high:

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                return self.sq(low, mid - 1, x)
            else:
                return self.sq(mid + 1, high, x)

        return mid

