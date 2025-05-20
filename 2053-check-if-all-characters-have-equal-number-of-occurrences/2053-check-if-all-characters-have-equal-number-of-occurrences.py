class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(s) <= 2: return True
        mp = defaultdict(int)
        for _ in s:
            mp[_] += 1
        temp = mp[s[0]]
        for value in mp.values():
            if temp != value:
                return False
        return True