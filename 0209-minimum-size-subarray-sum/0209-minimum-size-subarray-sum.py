class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = inf
        w = 0
        L = 0
        for R in range(len(nums)):
            w += nums[R]
            while w - nums[L] >= target:
                w -= nums[L]
                L += 1
            if w >= target:
                res = min(res, R-L+1)
        return res if res != inf else 0