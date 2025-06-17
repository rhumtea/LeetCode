class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        for r in range(row):
            for c in range(col):
                summ = count = 0
                for i in (r-1, r, r+1):
                    for j in (c-1, c, c+1):
                        if 0 <= i < row and 0 <= j < col:
                            summ += img[i][j] % 256
                            count += 1            
                img[r][c] += (summ // count) * 256
        for r in range(row):
            for c in range(col):
                img[r][c] //= 256
        return img