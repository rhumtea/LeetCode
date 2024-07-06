class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        str_n = str(n)
        l = len(str_n)
        for i in range(l):
            res += int(str_n[i])* (-1)**(i)
        return res
        