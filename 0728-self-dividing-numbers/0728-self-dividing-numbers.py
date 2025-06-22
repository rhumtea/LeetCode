class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            temp = num
            while temp > 0:
                d = temp%10
                if d == 0 or num%d != 0:
                    break
                temp //= 10
            if temp == 0:
                res.append(num)
        return res