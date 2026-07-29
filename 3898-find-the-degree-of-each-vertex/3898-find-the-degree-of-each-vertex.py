class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = defaultdict(int)
        n = len(matrix[0])
        for i in range(n):
            for j in range(n):
                if i <= j:
                    res[i] += matrix[i][j]
                    res[j] += matrix[i][j]
        return list(res.values())