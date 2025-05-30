class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        w = 0
        l = gap = 0
        for r in range(len(nums)):
            if nums[r]%2:
                w += 1
            if w == k:
                gap = 0
                while w == k:
                    if nums[l]%2:
                        w -= 1
                    gap += 1
                    l += 1
            res += gap
        return res                