class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        sum_largest = sum_smallest = 0
        nums.sort()
        n = len(nums)
        a = 0
        for i in range(n):
            sum_smallest += nums[i]
            sum_largest += nums[n-1 - i]
            a += 1
            if a == k: break
        return abs(sum_largest - sum_smallest)