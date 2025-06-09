class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        for i in range(k):
            summ += nums[i]
        max_avg = summ / k
        l = 0
        for i in range(k, len(nums)):
            summ = summ + nums[i] - nums[l]
            max_avg = max(max_avg, summ / k)
            l += 1
        return max_avg