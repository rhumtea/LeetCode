class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        w = defaultdict(int)
        l = 0
        for r in range(len(s)):
            w[s[r]] += 1
            while (r - l + 1) - max(w.values()) > k:
                w[s[l]] -= 1
                if w[s[l]] == 0:
                    del w[s[l]]
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length