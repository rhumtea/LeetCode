class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def max_k(x):
            res = l = w = 0
            for r in range(len(nums)):
                w += nums[r]%2
                while w > x:
                    w -= nums[l]%2
                    l += 1
                res += (r-l+1)
            return res
        return max_k(k) - max_k(k-1)