class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        nums = [0] + nums
        n = len(nums)
        pre = [0] * n
        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i]
        res = max_num = min_num = 0
        for r in range(1, n):
            res = max(res, pre[r] - min_num, max_num - pre[r])
            max_num = max(max_num, pre[r])
            min_num = min(min_num, pre[r])
        return res