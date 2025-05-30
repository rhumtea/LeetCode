class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        res = inf
        mp = defaultdict(int)
        for c in target:
            mp[c] += 1
        mp1 = defaultdict(int)
        for c in s:
            mp1[c] += 1
        for k, v in mp.items():
            res = min(res, mp1[k]//v)
        return res