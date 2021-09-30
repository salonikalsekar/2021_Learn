class Solution:
    def arraySign(self, nums: List[int]) -> int:
        isNeg = 0
        for i in nums:
            if i == 0:
                return 0

            elif i < 0:
                isNeg += 1

        return -1 if isNeg % 2 != 0 else 1

#         isZeroPresent = False
#         countNeg = 0
#         p = 1

#         for i in nums:
#             p *= i

#         def signFunc(p):
#             if p == 0:
#                 return 0

#             elif p < 0:
#                 return -1

#             else:
#                 return 1


#         return signFunc(p)