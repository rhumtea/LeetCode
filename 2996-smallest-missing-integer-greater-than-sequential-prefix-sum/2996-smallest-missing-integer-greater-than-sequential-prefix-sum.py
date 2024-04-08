class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sumSequence = nums[0]
        if len(nums) == 1:
            return sumSequence + 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1] + 1:
                sumSequence += nums[j]
            else:
                while sumSequence in nums:
                    sumSequence += 1
                return sumSequence
            if j == len(nums) - 1:
                return sumSequence