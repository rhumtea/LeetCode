class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = set()
        while len(nums) != 0:
            res.add((max(nums) + min(nums))/2)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return len(res)