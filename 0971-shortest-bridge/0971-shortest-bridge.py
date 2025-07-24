class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = [[False] * N for _ in range(N)]
        step = 0
        q = deque()
        def dfs(i, j):
            if visit[i][j] == True:
                return
            visit[i][j] = True
            if grid[i][j] == 1:
                grid[i][j] = 2
                q.append([i,j])
            for ni, nj in [[i+1, j], [i-1, j], [i,j+1], [i, j-1]]:
                if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == False:
                    if grid[ni][nj] == 1:
                        dfs(ni, nj)
        si = sj = -1
        found = False
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    si, sj = i, j
                    found = True
                    break
            if found:
                break
        dfs(si, sj)
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for ni, nj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                    if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == False:
                        if grid[ni][nj] == 1:
                            return step
                        else:
                            q.append([ni, nj])
                            visit[ni][nj] = True
            step += 1
        return step - 1