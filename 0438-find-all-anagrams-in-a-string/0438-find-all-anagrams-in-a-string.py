class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        mp_p = Counter(p)
        w = Counter(s[:np-1])
        res = []
        l = 0
        for r in range(np-1, ns):
            w[s[r]] += 1
            if w == mp_p: res.append(l)
            w[s[l]] -= 1
            if w[s[l]] == 0: del w[s[l]]
            l += 1
        return res