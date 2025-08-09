class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        count = 0
        visit = [[False] * N for _ in range(M)]
        def dfs(i, j):
            visit[i][j] = True
            for ni, nj in [[i+1,j], [i-1,j], [i, j+1], [i, j-1]]:
                if 0 <= ni < M and 0 <= nj < N and visit[ni][nj] == False and grid[i][j] == "1":
                    dfs(ni, nj)
        for i in range(M):
            for j in range(N): 
                if visit[i][j] == False and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count