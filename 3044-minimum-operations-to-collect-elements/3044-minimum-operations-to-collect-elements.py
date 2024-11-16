class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= k and nums[i] not in temp: temp.append(nums[i])
            if len(temp) == k: return len(nums) - i

        