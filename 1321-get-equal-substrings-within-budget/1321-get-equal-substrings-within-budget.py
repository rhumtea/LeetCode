class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        w = 0
        L = 0
        for R in range(len(s)):
            w += abs(ord(s[R]) - ord(t[R]))
            while w > maxCost:
                w -= abs(ord(s[L]) - ord(t[L]))
                L += 1
            res = max(res, R - L + 1)
        return res 
