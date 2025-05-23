class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        mp = defaultdict(int)
        for r in range(len(nums)):
            res += mp[nums[r]]
            mp[nums[r]] += 1
        return res