class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i] < k:
                count += 1
            else:
                return count
                