class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            u, l = upper - nums[i], lower - nums[i]
            res += bisect_right(nums, u, 0, i) - bisect_left(nums, l, 0, i)
        return res