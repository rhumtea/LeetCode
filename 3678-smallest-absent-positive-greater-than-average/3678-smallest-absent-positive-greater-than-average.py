class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        average = sum(nums) // len(nums)
        cur = max(1, average + 1)        
        nums = set(nums)
        while cur in nums:
            cur += 1
        return cur