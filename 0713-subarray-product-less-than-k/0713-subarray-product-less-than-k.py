class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        L = 0
        w = 1
        for R in range(len(nums)):
            w *= nums[R]
            while L <= R and w >= k:
                w //= nums[L]
                L += 1
            res += R - L + 1
        return res