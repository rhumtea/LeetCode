class Solution:
    def maxDifference(self, s: str) -> int:
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        max_odd = 0
        min_even = inf
        for v in mp.values():
            if v%2:
                max_odd = max(max_odd, v)
            else:
                min_even = min(min_even, v)
        return max_odd - min_even