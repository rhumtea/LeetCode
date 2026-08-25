class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        pref = [0] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = nums[i] + pref[i-1]
        res = 0
        mp = defaultdict(int)
        mp[0] = 1
        for r in range(1, len(pref)):
            t = pref[r] - k
            res += mp[t]
            mp[pref[r]] += 1
        return res 