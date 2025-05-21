class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def checkmap(temp_mp, mp):
            if len(temp_mp) > len(mp):
                return False
            for k, v in temp_mp.items():
                if k not in mp:
                    return False
                elif v > mp[k]:
                    return False
            return True
        res = 0
        mp = defaultdict(int)
        for c in chars:
            mp[c] += 1
        for word in words:
            temp_mp = defaultdict(int)
            for c in word:
                temp_mp[c] += 1
            if checkmap(temp_mp, mp):
                res += len(word)
        return res
    