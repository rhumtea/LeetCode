class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        def prefix_sum(nums):
            nums = [0] + nums
            prefix = [0] * len(nums)
            for i in range(1, len(prefix)):
                prefix[i] = prefix[i-1] + nums[i]
            return prefix
        prefix = prefix_sum(nums)
        res = min(prefix)
        return abs(res) + 1