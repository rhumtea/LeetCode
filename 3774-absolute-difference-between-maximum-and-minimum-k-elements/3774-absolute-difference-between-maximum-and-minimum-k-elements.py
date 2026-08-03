class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum_smallest = sum(nums[:k])
        sum_largest = sum(nums[len(nums)-k:])
        return abs(sum_largest - sum_smallest)