class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        arr = [0] + arr
        pre = [0] * len(arr)
        n = len(arr)
        for i in range(1, n):
            pre[i] = arr[i] + pre[i-1]
        cnt = {}
        ans = 0
        cnt[0] = 1
        for r in range(1, n):
            preL = pre[r]%2
            if preL in cnt: ans += cnt[preL]
            if pre[r]%2 in cnt: cnt[pre[r]%2] += 1
            else: cnt[pre[r]%2] = 1
        total_sub = ((n-1) * n) // 2
        return (total_sub - ans) % (10**9+7)