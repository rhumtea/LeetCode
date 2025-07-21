class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        def prefix_sum(arr):
            arr = [0] + arr
            prefix = [0] * len(arr)
            for i in range(1, len(arr)):
                prefix[i] = prefix[i-1] + arr[i]
            return prefix
        prefix = prefix_sum(nums)
        mp = defaultdict(int)
        res = 0
        for r in range(len(prefix)):
            res += mp[prefix[r]%k]
            mp[prefix[r]%k] += 1
        return res