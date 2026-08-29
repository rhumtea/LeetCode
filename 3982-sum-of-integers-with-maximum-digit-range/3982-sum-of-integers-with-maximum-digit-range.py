class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def digit_range(num):
            digits =  [int(ch) for ch in str(abs(num))]
            return max(digits) - min(digits)
        maxx = -1
        res = 0
        for num in nums:
            t = digit_range(num)
            if  t > maxx:
                maxx = t
                res =  num
            elif t == maxx:
                res += num
        return res