class Solution:
    def equalFrequency(self, word: str) -> bool:
        mp = defaultdict(int)
        for c in word:
            mp[c] += 1
        mp1 = defaultdict(int)
        for v in mp.values():
            mp1[v] += 1
        if len(mp1) == 1:
            return list(mp1.keys())[0] == 1 or list(mp1.values())[0] == 1
        if len(mp1) == 2:
            max_key = max(mp1.keys())
            min_key = min(mp1.keys())
            return ((max_key - min_key) == mp1[max_key] == 1) or (min_key == mp1[min_key] == 1)
        return False