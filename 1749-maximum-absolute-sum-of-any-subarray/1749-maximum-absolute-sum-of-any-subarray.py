class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        nums = [0] + nums
        pref = [0] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = nums[i] + pref[i-1]
        return max(pref) - min(pref)