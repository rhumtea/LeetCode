class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        w = defaultdict(int)
        l = 0
        max_freq = 0
        for r in range(len(s)):
            w[s[r]] += 1
            max_freq = max(max_freq, w[s[r]])
            if (r-l+1) - max_freq > k:
                w[s[l]] -= 1
                l += 1
        return len(s)-l