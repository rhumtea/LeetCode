class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closet = abs(nums[0])
        res = nums[0]
        for i in range(1, len(nums)):
            temp = abs(nums[i])
            if temp < closet:
                closet = temp
                res = nums[i]
            elif temp == closet and res < nums[i]:
                res = nums[i]
        return res
        