class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        exp = 0
        for i in range(len(columnTitle)-1, -1, -1):
            temp = ord(columnTitle[i]) - ord("A") + 1
            res += temp * 26**exp
            exp += 1
        return res 