class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        sumNum = 100
        while (left < right):
            sumNum = min(sumNum, nums[left] + nums[right])
            if nums[left] <= nums[right]:
                right -= 1
            else:
                left += 1
        return nums[0] + sumNum



