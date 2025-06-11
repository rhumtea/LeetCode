class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        new_mat = [[0] * c for _ in range(r)]
        row = column = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if column == c:
                    row += 1
                    column = 0
                new_mat[row][column] = mat[i][j]
                column += 1
        return new_mat