class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        count = 0
        visit = [[False] * N for _ in range(M)]
        def bfs(i, j):
            q = deque()
            visit[i][j] = True
            q.append([i, j])
            while q:
                a, b = q.popleft()
                for na, nb in [[a+1, b], [a-1, b], [a, b+1], [a, b-1]]:
                    if 0 <= na < M and 0 <= nb < N and visit[na][nb] == False and grid[na][nb] == "1":
                        q.append([na, nb])
                        visit[na][nb] = True
        for i in range(M):
            for j in range(N):
                if visit[i][j] == False and grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count