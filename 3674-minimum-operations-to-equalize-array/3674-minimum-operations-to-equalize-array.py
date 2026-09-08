class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a = nums[0]
        count = 0
        for num in nums:
            if num == a: count += 1
        return 1 if count < len(nums) else 0