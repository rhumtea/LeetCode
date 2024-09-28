class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxSum = 0
        length = len(nums)
        for i in range (length - 1):
            digit1 = max(str(nums[i]))
            for j in range(i+1, length):
                digit2 = max(str(nums[j]))
                if digit1 == digit2:
                    maxSum = max(maxSum, nums[i] + nums[j])
        return -1 if maxSum == 0 else maxSum