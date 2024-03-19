class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        #Use Basic Binary Search
        first = 0
        last = len(nums) - 1
        while first <= last:
            midIndex = (first + last) // 2
            if nums[midIndex] == target:
                return midIndex
            elif nums[midIndex] < target:
                first = midIndex + 1
            else:
                last = midIndex - 1
        return -1

        