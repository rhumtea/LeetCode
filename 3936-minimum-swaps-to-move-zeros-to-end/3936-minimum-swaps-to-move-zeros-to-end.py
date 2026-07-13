class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        zero = nums.count(0)
        for i in range(n):
            if nums[i] == 0 and i < n - zero:
                res += 1
        return res