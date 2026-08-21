class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        pref = [0] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = nums[i] + pref[i-1]

        count = defaultdict(int)
        count[0] = 1
        res = 0
        for r in range(1,  len(nums)):
            t = pref[r] - k
            res += count[t]
            count[pref[r]] += 1
        return res