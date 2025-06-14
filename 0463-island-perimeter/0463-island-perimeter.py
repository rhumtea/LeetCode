class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cur = grid[row][col]
                if cur:
                    res += cur * 4
                    if row > 0:
                        res -= cur * grid[row-1][col]
                    if col > 0:
                        res -= cur * grid[row][col-1]
                    if row < len(grid)-1:
                        res -= cur * grid[row+1][col]
                    if col < len(grid[0])-1:
                        res -= cur * grid[row][col+1]                 
        return res