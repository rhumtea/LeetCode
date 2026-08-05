class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        a = b = -101
        c = 101
        for num in nums:
            if a < num:
                b = a
                a = num
            elif b < num:
                b = num
            if c > num:
                c = num
        return a+b-c