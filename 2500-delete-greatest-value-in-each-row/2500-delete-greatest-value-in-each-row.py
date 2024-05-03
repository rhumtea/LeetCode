class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid: row.sort()
        for col in zip(*grid):
            res += max(col)
        return res