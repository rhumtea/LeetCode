class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        SortedList(nums)
        if target not in nums:
            return [-1, -1]
        else:
            a = bisect_left(nums, target)
            numOfTarget = bisect_right(nums, target) - bisect_left(nums, target)
        return [a, a+numOfTarget-1]