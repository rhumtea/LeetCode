class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        nums = [0] + nums
        pref = [0] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = nums[i] + pref[i-1]
        k = sum(nums) - x
        if k == 0: return n
        res = -1
        mp = {}
        mp[0] = 0
        for r in range(1, len(pref)):
            t = pref[r] - k
            if t in mp: res = max(res, r - mp[t])
            if pref[r] not in mp: mp[pref[r]] = r
        return -1 if res == -1 else n-res