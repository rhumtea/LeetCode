class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        nums = [0] + nums
        n = len(nums)
        pre = [0] * n
        for i in range(1, n):
            pre[i] = nums[i] + pre[i-1]
        res = minn = maxx = 0
        for r in range(1, n):
            res = max(res, pre[r] - minn, maxx - pre[r])
            minn = min(minn, pre[r])
            maxx = max(maxx, pre[r])
        return res