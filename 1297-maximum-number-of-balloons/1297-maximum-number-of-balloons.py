class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = defaultdict(int)
        word = "balloon"
        for c in word:
            mp[c] += 1
        mp1 = defaultdict(int)
        for c in text:
            mp1[c] += 1
        res = inf
        for k, v in mp.items():
            res = min(res, mp1[k] // v)
        return res