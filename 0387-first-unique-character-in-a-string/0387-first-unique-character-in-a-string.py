class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        for k, v in mp.items():
            if v == 1:
                return s.index(k)
        return -1