class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        res = [[0] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                summ = count = 0
                for i in (r-1, r, r+1):
                    for j in (c-1, c, c+1):
                        if 0 <= i < row and 0 <= j < col:
                            summ += img[i][j]
                            count += 1            
                res[r][c] = summ // count
        return res