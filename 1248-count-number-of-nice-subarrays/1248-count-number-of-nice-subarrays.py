class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def max_k(x):
            res = w = 0
            l = 1
            for r in range(1, len(nums)):
                w += nums[r]%2
                while w > x:
                    w -= nums[l]%2
                    l += 1
                res += (r-l+1)
            return res
        n = len(nums)
        nums = [0] + nums
        return max_k(k) - max_k(k-1)