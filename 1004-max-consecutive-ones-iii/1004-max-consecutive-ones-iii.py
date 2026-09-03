class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        w = {0:0,1:0}
        l = 0
        for r in range(len(nums)):
            w[nums[r]] += 1
            while w[0] > k:
                w[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res