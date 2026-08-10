class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            if target - nums[i] not in a:
                a[nums[i]] = i
            else:
                return [i, a[target - nums[i]]]