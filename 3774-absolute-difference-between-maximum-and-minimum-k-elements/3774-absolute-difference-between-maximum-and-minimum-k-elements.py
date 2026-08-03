class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        sum_largest = sum_smallest = 0
        nums.sort()
        a = 0
        for i in range(len(nums)):
            sum_smallest += nums[i]
            a += 1
            if a == k: break
        for i in range(len(nums)-1, -1,-1):
            sum_largest += nums[i]
            a -= 1
            if a == 0: break
        return abs(sum_largest - sum_smallest)