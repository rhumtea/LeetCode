class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mp_p = Counter(p)
        n = len(p)
        w = Counter(s[:n])
        res = []
        l = 0
        if w == mp_p: res.append(l)
        for r in range(n, len(s)):
            w[s[r]] += 1
            w[s[l]] -= 1
            if w[s[l]] == 0: del w[s[l]]
            l += 1
            if w == mp_p: res.append(l)
        return res