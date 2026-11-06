class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [0] + nums
        n = len(nums)
        pre = [0] * n
        for i in range(1, n):
            pre[i] = nums[i] + pre[i-1]
        mp = defaultdict(int)
        mp[0], res = 0, 0
        for r in range(1, n):
            t = r - 2 * pre[r]
            if t in mp: res = max(res, r - mp[t])
            if t not in mp: mp[t] = r
        return res