class Solution:
    def climbStairs(self, n: int) -> int:
        mp = defaultdict(int)
        mp[1] = 1
        mp[2] = 2
        if n in mp:
            return mp[n]
        for i in range(3, n+1):
            mp[i] = mp[i-1] + mp[i-2]
        return mp[n]