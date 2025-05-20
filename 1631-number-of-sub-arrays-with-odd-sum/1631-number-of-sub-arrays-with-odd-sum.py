class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        def prefix_sum(arr):
            prefix = [0] * len(arr)
            prefix[0] = arr[0]
            for i in range(1, len(arr)):
                prefix[i] = prefix[i-1] + arr[i]
            return prefix
        prefix = prefix_sum(arr)
        mp = defaultdict(int)
        mp[0] = 1
        res = 0
        for r in range(len(prefix)):
            temp = prefix[r] % 2
            if temp == 1:
                res += mp[0]
            else:
                res += mp[1]
            mp[prefix[r] % 2] += 1
        return res % (10**9 + 7)