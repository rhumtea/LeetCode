class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        res = set()
        while len(nums) != 0:
            res.add((nums[0] + nums[-1])/2)
            nums.pop(0)
            nums.pop(-1)
        return len(res)