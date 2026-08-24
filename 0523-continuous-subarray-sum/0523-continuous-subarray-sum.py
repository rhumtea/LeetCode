class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        nums = [0] + nums
        pref = [0] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = nums[i] + pref[i-1]
        
        mp = {}
        mp[0] = 0
        for r in range(1, len(pref)):
            t = pref[r] % k
            if t in mp and r - mp[t] >= 2: return True
            if t not in mp: mp[t] = r
        return False