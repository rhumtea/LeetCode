class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        res = 0
        for num in nums:
            if min_num < num < max_num:
                res += 1 
        return res