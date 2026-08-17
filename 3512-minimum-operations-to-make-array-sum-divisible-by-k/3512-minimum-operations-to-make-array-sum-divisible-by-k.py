class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        summ = 0
        for num in nums:
            summ += num
        return summ%k