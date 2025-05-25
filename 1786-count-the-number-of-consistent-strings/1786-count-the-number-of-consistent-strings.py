class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mp = defaultdict(int)
        for c in allowed:
            mp[c] += 1
        res = 0
        for word in words:
            check = True
            for c in word:
                if c not in mp:
                    check = False
                    break
            if check:
                res += 1
        return res