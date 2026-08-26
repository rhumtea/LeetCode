class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                a, b = nums[i], nums[j]
                t = (a*b)/(gcd(a,b))**2
                res = max(res, t)
        return int(res)