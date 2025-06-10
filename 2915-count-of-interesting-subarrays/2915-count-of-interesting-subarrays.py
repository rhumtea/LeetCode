class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        def prefix_sum(arr):
            arr = [0] + arr
            prefix = [0] * len(arr)
            for i in range(1, len(arr)):
                prefix[i] = prefix[i-1] + arr[i]
            return prefix
        new_nums = [1 if (num % modulo == k) else 0 for num in nums]
        prefix = prefix_sum(new_nums)
        mp = defaultdict(int)
        res = 0
        for r in range(len(prefix)):
            temp = (prefix[r] - k) % modulo
            res += mp[temp]
            mp[prefix[r] % modulo] += 1
        return res