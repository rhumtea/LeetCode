class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        nums = [0] + nums
        pref = [0] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = nums[i] + pref[i-1]
        res = minn = maxx = 0
        for r in range(1, len(pref)):
            t = pref[r]
            res = max(res, t - minn, maxx - t)
            minn = min(minn, t)
            maxx = max(maxx, t)
        return res