class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        index = 0
        if nums == sorted(nums): return 0
        for i in range(1, len(nums)):
            if nums[i-1]  < nums[i]: continue
            else: index = i
        newNums = nums[index:] + nums[0:index]
        print(newNums)
        print(sorted(nums))
        if newNums == sorted(nums): return len(nums) - index
        else: return -1