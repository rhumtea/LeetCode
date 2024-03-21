class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(a):
            maxDigit = a % 10
            base = 1
            a //= 10
            while a != 0:
                if a%10 > maxDigit:
                    maxDigit = a%10
                base = base*10+1
                a //= 10
            return maxDigit * base
        sum = 0
        for i in range(len(nums)):
            sum += encrypt(nums[i])
        return sum