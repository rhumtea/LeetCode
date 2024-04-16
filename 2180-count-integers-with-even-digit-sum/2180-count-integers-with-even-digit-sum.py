class Solution:
    def countEven(self, num: int) -> int:
        tensNearNum = num // 10 * 10
        count = num // 10 * 5 
        for i in range(tensNearNum, num+1):
            sumDigit = 0
            while i != 0:
                sumDigit += i%10
                i //= 10
            if sumDigit % 2 == 0:
                count += 1
        return count-1 #exclude 0