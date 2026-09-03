class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mp = Counter(p)
        n = len(p)
        w = Counter(s[:(n-1)])
        l = 0
        res = []
        for r in range(n-1, len(s)):
            w[s[r]] += 1
            if w == mp: res.append(l)
            w[s[l]] -= 1
            if w[s[l]] == 0: del w[s[l]]
            l += 1
        return res