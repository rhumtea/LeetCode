class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxx = 0
        w = defaultdict(int)
        l = 0
        for r in range(len(s)):
            w[s[r]] += 1
            while (r-l+1) - max(w.values()) > k:
                w[s[l]] -= 1
                l += 1
            maxx = max(maxx, r-l+1)
        return maxx