class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        w = defaultdict(int)
        l = 0
        freq = 0
        for r in range(len(s)):
            w[s[r]] += 1
            freq = max(freq, w[s[r]])
            if (r-l+1) - freq > k:
                w[s[l]] -= 1
                l += 1
        return len(s)-l