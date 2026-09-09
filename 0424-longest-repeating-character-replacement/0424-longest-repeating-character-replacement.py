class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        w = defaultdict(int)
        l = 0
        for r in range(len(s)):
            w[s[r]] += 1
            while (r-l+1) - max(w.values()) > k:
                w[s[l]] -= 1
                l += 1
            max_freq = max(max_freq, r-l+1)
        return max_freq