class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        left = nums[0]
        for i in range(1, len(nums)-1):
            if left < nums[i] > nums[i+1] or left > nums[i] < nums[i+1]:
                left = nums[i]
                count += 1
        return count