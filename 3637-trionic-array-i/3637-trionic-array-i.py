class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        peak = 0
        if nums[1] <= nums[0]: return False
        for i in range(1, len(nums)-1):
            if (
                (nums[i] > nums[i-1] and nums[i] > nums[i+1]) 
                or (nums[i] < nums[i-1] and nums[i] < nums[i+1])
            ):
                peak +=1
            if nums[i] == nums[i+1]:
                return False
        return peak == 2