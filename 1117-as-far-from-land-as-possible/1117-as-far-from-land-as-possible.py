class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        step = 0
        visit = [[False] * N for _ in range(N)]
        q = deque()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append([i, j])
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == False and grid[ni][nj] == 0:
                        q.append([ni, nj])
                        visit[ni][nj] = True
            step += 1
        return -1 if step == 0 or step == 1 else step - 1