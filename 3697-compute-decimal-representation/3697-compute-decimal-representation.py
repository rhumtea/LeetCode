class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        if n % 10 != 0: res.append(n%10)
        n //= 10
        t = 1
        while n > 0:
            t *= 10
            if n%10 != 0: res.append(n%10 * t)
            n //= 10
        res.sort(reverse=True)
        return res