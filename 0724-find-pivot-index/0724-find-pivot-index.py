class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        prefix_sum = 0
        for i in range(len(nums)):
            if prefix_sum == summ - prefix_sum - nums[i]:
                return i
            prefix_sum += nums[i]
        return -1