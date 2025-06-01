class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        mp = defaultdict(int)
        for hour in hours:
            print("hour", hour%24)
            if (24 - hour%24) in mp:
                res += mp[24 - hour%24]
            if hour%24 == 0 and hour%24 in mp:
                res += mp[0]
            mp[hour%24] += 1
        return res