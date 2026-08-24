class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [0] + nums
        pref = [0] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = nums[i] + pref[i-1]

        mp = defaultdict(int)
        mp[0] = 0
        res = 0
        for r in range(1, len(pref)):
            t = r - 2 * pref[r]
            if t in mp: res = max(res, r - mp[t])
            if t not in mp: mp[t] = r
        return res