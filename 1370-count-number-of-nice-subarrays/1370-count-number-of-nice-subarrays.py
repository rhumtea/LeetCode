class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            res = l = w = 0
            for r in range(len(nums)):
                if nums[r]%2: w += 1
                while w > k:
                    if nums[l]%2: w -= 1
                    l += 1
                res += r-l+1
            return res
        a = helper(nums, k)
        b = helper(nums, k-1)
        return a-b

        
