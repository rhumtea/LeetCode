class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        mp = defaultdict(int)
        for word in words:
            temp = SortedSet()
            for c in word:
                temp.add(c)
            temp = ''.join(temp)
            mp[temp] += 1
        for value in mp.values():
            if value >= 2:
                res += (value * (value - 1) // 2)
        return res