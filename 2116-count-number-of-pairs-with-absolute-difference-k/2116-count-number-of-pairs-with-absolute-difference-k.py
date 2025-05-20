class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        mp = defaultdict(int)
        for num in nums:
            a = num - k
            b = num + k
            if a in mp:
                res += mp[a]
            if b in mp:
                res += mp[b]
            mp[num] += 1
        return res