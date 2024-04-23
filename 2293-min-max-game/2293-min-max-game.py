class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def helper(i, num1, num2):
            return max(num1, num2) if i%2 else min(num1, num2)
        if len(nums) < 2:
            return nums[0]
        while len(nums) > 1:
            n = len(nums) // 2
            newNums = [helper(i, nums[2*i], nums[2*i+1]) for i in range(n)]
            nums = newNums
        return nums[0]
            
        


