class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = inf
        l = 0
        w = 0
        for r in range(len(nums)):
            w += nums[r]
            while w - nums[l] >= target:
                w -= nums[l]
                l += 1
            if w >= target:
                res = min(res, r-l+1)
        return res if res != inf else 0