class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        count = 0
        visit = [[False] * N for _ in range(M)]
        def bfs(si, sj):
            q = deque()
            visit[si][sj] = True
            q.append([si, sj])
            while q:
                i, j = q.popleft()
                for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= ni < M and 0 <= nj < N and visit[ni][nj] == False and grid[ni][nj] == "1":
                        q.append([ni, nj])
                        visit[ni][nj] = True
        for si in range(M):
            for sj in range(N):
                if visit[si][sj] == False and grid[si][sj] == "1":
                    count += 1
                    bfs(si, sj)
        return count