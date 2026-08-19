class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_val = max(nums)
        if max_val <= 0: return max_val
        nums = set(nums)
        summ = 0
        for num in nums:
            if num > 0: summ += num
        return summ