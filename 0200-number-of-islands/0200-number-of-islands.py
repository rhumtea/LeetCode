class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        p = list(range(M*N))
        size = [1] * (M*N)
        R = [0] * (M*N)
        def find(i, j):
            d = i * N + j
            while d != p[d]:
                d = p[d]
            return d
        def union(ui, uj, vi, vj):
            du, dv = find(ui, uj), find(vi, vj)
            if du == dv:
                return False
            if R[du] < R[dv]:
                du, dv = dv, du
            p[dv] = du
            size[du] += size[dv]
            if R[du] == R[dv]:
                R[du] += 1
            return True
        count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '0':
                    count += 1
                    continue
                for ni, nj in [[i-1, j], [i, j-1]]:
                    if 0 <= ni < M and 0 <= nj < N and grid[i][j] == grid[ni][nj]:
                        union(i, j, ni, nj)
        res = set()
        for i in range(M):
            for j in range(N):
                res.add(find(i, j))
        return len(res) - count