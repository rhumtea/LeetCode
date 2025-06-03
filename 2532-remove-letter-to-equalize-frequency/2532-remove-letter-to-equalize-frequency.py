class Solution:
    def equalFrequency(self, word: str) -> bool:
        mp = defaultdict(int)
        for c in word:
            mp[c] += 1
        for c in word:
            mp[c] -= 1
            if mp[c] == 0:
                mp.pop(c)
            if len(set(mp.values())) == 1:
                return True
            mp[c] += 1
        return False