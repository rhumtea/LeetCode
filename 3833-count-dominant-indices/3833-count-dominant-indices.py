class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        res = 0
        for i in range(len(nums)):
            total -= nums[i]
            n -= 1
            if n > 0 and nums[i] > total/n:
                res += 1
        return res