class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        w = defaultdict(int)
        mp = defaultdict(int)
        for c in p:
            mp[c] += 1
        l = 0
        n = len(p)
        for r in range(len(s)):
            w[s[r]] += 1
            while (r-l+1) > n:
                w[s[l]] -= 1
                if w[s[l]] == 0:
                    w.pop(s[l])
                l += 1
            if w == mp:
                res.append(l)
        return res