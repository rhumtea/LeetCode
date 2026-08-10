class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        t = 1
        while n > 0:
            digit = n%10
            if digit != 0: res.append(digit * t)
            n //= 10
            t *= 10
        return res[::-1]