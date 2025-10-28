class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        res, prev = 0, 0
        for i in range(m):
            temp = bank[i].count('1')
            res += temp * prev
            if temp > 0:
                prev = temp
        return res