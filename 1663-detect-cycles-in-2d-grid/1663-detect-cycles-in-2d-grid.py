class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        visited = [[False] * N for _ in range(M)]
        def dfs(i, j, pi, pj):
            if visited[i][j] == True:
                return True
            visited[i][j] = True
            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= ni < M and 0 <= nj < N and [ni, nj] != [pi, pj] and grid[ni][nj] == grid[i][j]:
                    if dfs(ni, nj, i, j):
                        return True   
            return False 
        for si in range(M):
            for sj in range(N):
                if visited[si][sj] == False:
                    if dfs(si, sj, -1, -1):
                        return True
        return False
                    