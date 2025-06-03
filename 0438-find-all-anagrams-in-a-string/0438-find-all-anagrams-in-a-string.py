class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        res = []
        w = defaultdict(int)
        mp = defaultdict(int)
        n = len(p)
        for i in range(n):
            mp[p[i]] += 1
            w[s[i]] += 1
        if w == mp:
            res.append(0)
        l = 0
        for i in range(n, len(s)):
            w[s[i]] += 1
            w[s[l]] -= 1
            if w[s[l]] == 0:
                w.pop(s[l])
            l += 1
            if w == mp:
                res.append(l)
        return res