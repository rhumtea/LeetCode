class Solution:
    def maxScore(self, s: str) -> int:
        summ = 0
        for c in s:
            summ += int(c)
        mp = defaultdict(int)
        res = 0
        for i in range(len(s)-1):
            mp[int(s[i])] += 1
            res = max(res, mp[0] + summ - mp[1])
        return res