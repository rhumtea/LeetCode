class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = summ = w = l = 0
        for r in range(len(nums)):
            summ += nums[r]
            w = summ * (r - l + 1)
            while w >= k:
                summ -= nums[l]
                l += 1
                w = summ * (r - l + 1)
            res += r - l + 1
        return res