class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        w = SortedList()
        l = 0
        res = 0
        for r in range(len(nums)):
            w.add(nums[r])
            while w[-1] - w[0] > limit:
                w.discard(nums[l])
                l += 1
            if w[-1] - w[0] <= limit:
                res = max(res, r-l+1)
        return res