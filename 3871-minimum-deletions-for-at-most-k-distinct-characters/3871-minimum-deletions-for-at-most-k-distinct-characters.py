class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        res = 0
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        m = len(mp)
        for key, v in sorted(mp.items(), key = lambda x:x[1]):
            if m > k:
                res += v
                m -= 1
        return res