class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        print("aaaaa", nums)
        right = 0
        for left in range(len(nums)):
            if nums[left] != 0: 
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
        return nums