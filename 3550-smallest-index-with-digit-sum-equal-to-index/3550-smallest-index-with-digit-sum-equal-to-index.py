class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_digit(n):
            sum_digit = 0
            while n > 0:
                sum_digit += n % 10
                n //= 10
            return sum_digit
        for i in range(len(nums)):
            if i == sum_digit(nums[i]):
                return i
        return -1