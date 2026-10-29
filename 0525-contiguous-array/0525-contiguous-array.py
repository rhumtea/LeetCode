class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [0] + nums
        pre = [0] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = nums[i] + pre[i-1]
        mp = defaultdict(int)
        mp[0], res = 0, 0
        for r in range(1, len(pre)):
            t = r - 2 * pre[r]
            if t in mp: res = max(res, r - mp[t])
            if t not in mp: mp[t] = r
        return res