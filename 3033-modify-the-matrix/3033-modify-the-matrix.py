class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = matrix
        m = len(matrix)
        n = len(matrix[0])
        for col in range (n):
            maxCol = 0
            # find max in column
            for row in range(m):
                maxCol = max(maxCol, answer[row][col])
            # find -1
            for row in range(m):
                if answer[row][col] == -1:
                    answer[row][col] = maxCol
        return answer

        