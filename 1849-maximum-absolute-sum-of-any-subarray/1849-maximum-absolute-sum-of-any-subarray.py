class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def prefix_sum(nums):
            prefix = [0] * len(nums)
            prefix[0] = nums[0]
            for i in range(1, len(nums)):
                prefix[i] = prefix[i-1] + nums[i]
            return prefix
        res = 0
        prefix = prefix_sum(nums)
        max_num = max(-inf, 0) #mang trong => prefix = 0
        min_num = min(inf, 0)
        for r in range(len(prefix)):
            temp = abs(prefix[r] - min_num)
            temp1 = abs(prefix[r] - max_num)
            res = max(res, temp, temp1)
            max_num = max(max_num, prefix[r])
            min_num = min(min_num, prefix[r])
        return res