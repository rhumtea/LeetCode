class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set_num = set(nums)
        for i in range(k, 20000, k):
            if i not in set_num:
                return i
        return k

