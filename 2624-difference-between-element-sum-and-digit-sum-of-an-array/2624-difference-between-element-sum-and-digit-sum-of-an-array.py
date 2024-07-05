class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumNum = 0
        sumDigit = 0
        if nums == None: return 0
        for i in nums: 
            sumNum += i
            temp = i
            while temp > 0:
                sumDigit += temp%10
                temp //= 10
        return abs(sumNum - sumDigit)
