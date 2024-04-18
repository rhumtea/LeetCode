class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1, col2 = ord(s[0]), ord(s[3])
        row1, row2 = int(s[1]), int(s[4])
        res = []
        for i in range(col1, col2 + 1):
            for j in range(row1, row2 + 1):
                temp = chr(i) + str(j)
                res.append(temp)
                # res.append(f'{chr(i)}{j}')
        return res