class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negative = [nums[i] for i in range(len(nums)) if nums[i] < 0]
        k = 0
        for i in range(len(nums)):
            if nums[i] > k and -nums[i] in negative:
                k = nums[i]
        return k if k != 0 else -1