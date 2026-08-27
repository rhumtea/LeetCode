class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = l = w = 0
        for r in range(len(s)):
            a = abs(ord(s[r]) - ord(t[r]))
            w += a
            while w > maxCost:
                b = abs(ord(s[l]) - ord(t[l]))
                w -= b
                l += 1
            res = max(res, r-l+1)
        return res