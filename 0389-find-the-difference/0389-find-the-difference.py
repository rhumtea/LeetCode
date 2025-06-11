class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = defaultdict(int)
        for c in t:
            mp[c] += 1
        for c in s:
            mp[c] -= 1
            if mp[c] == 0:
                del mp[c]
        for key in mp.keys():
            return key