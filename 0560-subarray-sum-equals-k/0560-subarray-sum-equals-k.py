class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def prefix_sum(nums):
            prefix = [0] * len(nums)
            prefix[0] = nums[0]
            for i in range(1, len(nums)):
                prefix[i] = prefix[i - 1] + nums[i]
            return prefix
        prefix = prefix_sum(nums)
        res = 0
        mp = defaultdict(int)
        mp[0] = 1 # subarray trống 
        for i in range(len(prefix)):
            temp = prefix[i] - k
            res += mp[temp]
            mp[prefix[i]] += 1
        return res