class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        l = len(nums) - 1
        ans = nums
        while l >= 0:
            ans.append(nums[l])
            l -= 1
        return ans