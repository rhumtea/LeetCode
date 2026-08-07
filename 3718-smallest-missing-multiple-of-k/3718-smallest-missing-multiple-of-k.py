class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set_num = set(nums)
        start = k
        while start in set_num:
            start += k
        return start