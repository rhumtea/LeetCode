class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = set(nums)
        nums = list(nums)
        nums.sort(reverse=True)
        return nums[:k]