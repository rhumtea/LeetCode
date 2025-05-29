class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        res = inf
        n = len(nums)
        w = 0
        l = 0
        summ = sum(nums)
        for r in range(n):
            w += nums[r]
            while l <= r and w > summ - x:
                w -= nums[l]
                l += 1
            if w == summ - x:
                res = min(res, n - (r - l + 1))
        return -1 if res == inf else res