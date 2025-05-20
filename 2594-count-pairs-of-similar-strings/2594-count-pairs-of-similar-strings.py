class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        mp = defaultdict(int)
        for word in words:
            temp = set()
            for c in word:
                temp.add(c)
            temp = list(temp)
            temp.sort()
            temp = ''.join(temp)
            res += mp[temp]
            mp[temp] += 1
        return res