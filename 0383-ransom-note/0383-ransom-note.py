class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = defaultdict(int)
        for c in magazine:
            mp[c] += 1
        mp1 = defaultdict(int)
        for c in ransomNote:
            mp1[c] += 1
        for k, v in mp1.items():
            if k not in mp or mp[k] < v:
                return False
        return True