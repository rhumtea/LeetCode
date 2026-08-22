class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        arr = [0] + arr
        pref = [0] * len(arr)
        for i in range(1, len(arr)):
            pref[i] = arr[i] + pref[i-1]
        count = defaultdict(int)
        ans = 0
        count[0] = 1
        for r in range(1, len(arr)):
            t = pref[r] % 2
            ans += count[t]
            count[t] += 1
        n = len(arr) - 1
        sum_sub = (n * (n+1)) // 2
        return (sum_sub - ans) %  (10**9 + 7)