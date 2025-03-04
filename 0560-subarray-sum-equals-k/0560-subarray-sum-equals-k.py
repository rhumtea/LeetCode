class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = [0]
        mp = defaultdict(int)
        for num in nums:
            prefix.append(prefix[-1]+num)
        for r in range(len(prefix)):
            if prefix[r] - k in mp:
                res += mp[prefix[r]-k]
            mp[prefix[r]] += 1
        return res
            

