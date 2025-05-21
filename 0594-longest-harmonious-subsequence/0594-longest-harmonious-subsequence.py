class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        l = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                res = max(res, r - l + 1)
        return res