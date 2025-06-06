class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            res += bisect_right(nums, upper - nums[i], 0, i) - bisect_left(nums, lower - nums[i], 0, i)
        return res