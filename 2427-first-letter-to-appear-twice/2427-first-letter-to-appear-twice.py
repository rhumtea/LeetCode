class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
            if mp[c] == 2:
                return c