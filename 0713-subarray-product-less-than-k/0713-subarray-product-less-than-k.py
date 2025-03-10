class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        res = 0
        l = 0
        w = 1
        for r in range(len(nums)):
            w *= nums[r]
            print(w)
            while w >= k:
                w //= nums[l]
                l += 1
            res += r-l+1
        return res