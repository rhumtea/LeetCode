class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def digit_range(num):
            smallest = 10
            largest = -1
            while num > 0:
                d = num%10
                smallest = min(smallest, d)
                largest =  max(largest, d)
                num //= 10
            return largest - smallest

        res = 0
        mp = defaultdict(list)
        max_digit = 0
        for num in nums:
            t = digit_range(num)
            mp[t].append(num)
            max_digit = max(max_digit, t)
        return sum(mp[max_digit])