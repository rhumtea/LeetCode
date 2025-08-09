class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        count = 0
        visit = [[False] * N for _ in range(M)]
        def bfs(s_i, s_j):
            q = deque()
            visit[s_i][s_j] = True
            q.append([s_i, s_j])
            while q:
                i, j = q.popleft()
                for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= ni < M and 0 <= nj < N and visit[ni][nj] == False and grid[ni][nj] == "1":
                        q.append([ni, nj])
                        visit[ni][nj] = True
        for s_i in range(M):
            for s_j in range(N):
                if visit[s_i][s_j] == False and grid[s_i][s_j] == "1":
                    count += 1
                    bfs(s_i, s_j)
        return count