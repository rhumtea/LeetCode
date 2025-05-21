class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        def prefix_sum(nums):
            prefix = [0] * len(nums)
            prefix[0] = nums[0]
            for i in range(1, len(nums)):
                prefix[i] = prefix[i-1] + nums[i]
            return prefix
        prefix = prefix_sum(nums)
        mp = defaultdict(int)
        mp[0] = -1
        for r in range(len(prefix)):
            # len of subarray >= 2 => find max of len of subarray for each prefix[r]%k
            if prefix[r]%k in mp and r - mp[prefix[r]%k] >= 2:
                return True
            if prefix[r]%k not in mp:     
                mp[prefix[r]%k] = r
        return False