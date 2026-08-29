class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        nums = [0] + nums
        w = {0:0, 1:0}
        l = 1
        for r in range(1, n+1):
            w[nums[r]] += 1
            while w[0] > k:
                w[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res