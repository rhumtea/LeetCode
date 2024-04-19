class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closet = abs(nums[0])
        res = nums[0]
        for num in nums:
            temp = abs(num)
            if temp < closet:
                closet = temp
                res = num
            elif temp == closet:
                res = max(res, num)
        return res
        