class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_digit(n):
            sum_digit = 0
            while n > 0:
                sum_digit += n % 10
                n //= 10
            return sum_digit
        res = inf
        for i in range(len(nums)):
            if i == sum_digit(nums[i]):
                res = min(res, i)
        return -1 if res == inf else res