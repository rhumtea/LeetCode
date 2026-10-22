class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        pre = [0] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = nums[i] + pre[i-1]
        cnt = {}
        cnt[0] = 1
        res = 0
        for r in range(1, len(pre)):
            preL = pre[r] - k
            if preL in cnt: res += cnt[preL]
            if pre[r] not in cnt: cnt[pre[r]] = 1
            else: cnt[pre[r]] += 1
        return res