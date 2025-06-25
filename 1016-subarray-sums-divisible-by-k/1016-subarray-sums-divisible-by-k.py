class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        def prefix_sum(nums):
            nums = [0] + nums
            prefix = [0] * len(nums)
            for i in range(1, len(nums)):
                prefix[i] = prefix[i-1] + nums[i]
            return prefix
        prefix = prefix_sum(nums)
        mp = defaultdict(int)
        res = 0
        for p in prefix:
            res += mp[p%k]
            mp[p%k] += 1
        return res