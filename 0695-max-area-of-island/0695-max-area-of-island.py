class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        p = list(range(M*N))
        size = [1] * (M*N)
        R = [0] * (M*N)
        def helper(i, j):
            d = i * N + j
            return d
        def find(u):
            while u != p[u]:
                u = p[u]
            return u
        def union(u, v):
            u, v = find(u), find(v) 
            if u == v:
                return False
            if R[u] < R[v]:
                u, v = v, u
            p[v] = u
            size[u] += size[v]
            if R[u] == R[v]:
                R[u] += 1
            return True
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    continue
                u = helper(i, j)
                for ni, nj in [[i-1, j], [i, j-1]]:
                    v = helper(ni, nj)
                    if 0 <= ni < M and 0 <= nj < N and grid[i][j] == grid[ni][nj]:
                        union(u, v)
        res = 0
        for i in range(M):
            for j in range(N):
                u = helper(i, j)
                if grid[i][j] == 1:
                    res = max(res, size[find(u)])
        return res