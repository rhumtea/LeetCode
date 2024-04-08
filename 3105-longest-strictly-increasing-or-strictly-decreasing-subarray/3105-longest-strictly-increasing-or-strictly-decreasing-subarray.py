class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLen = maxLenIncrease = maxLenDecrease = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                maxLenIncrease += 1
                maxLenDecrease = 1
            elif nums[i] > nums[i+1]:
                maxLenIncrease = 1
                maxLenDecrease += 1
            else:
                maxLenIncrease = 1
                maxLenDecrease = 1
            maxLen = max(maxLen, maxLenIncrease, maxLenDecrease)
        return maxLen
                
                