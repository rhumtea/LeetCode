class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        one = two = -1
        res = 100
        for i in range(len(nums)):
            if nums[i] == 1: one = i
            elif nums[i] == 2: two = i
            if one != -1 and two != -1:
                res = min(res, abs(one - two))
        return -1 if res == 100 else res