class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        p = defaultdict(tuple)
        size = defaultdict(int)
        R = defaultdict(int)
        def find(u):
            if u not in p:
                p[u] = u
                size[u] = 1
                R[u] = 0
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
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j > 0:
                    a = (i, j, 'L')
                    b = (i, j-1, 'R')
                    union(a, b)
                if i > 0:
                    a = (i, j, 'T')
                    b = (i-1, j, 'B')
                    union(a, b)
                if grid[i][j] == "/":
                    union((i, j, 'T'), (i, j, 'L'))
                    union((i, j, 'B'), (i, j, 'R'))
                elif grid[i][j] == " ":
                    union((i, j, 'T'), (i, j, 'L'))
                    union((i, j, 'B'), (i, j, 'R'))
                    union((i, j, 'T'), (i, j, 'R'))
                else:
                    union((i, j, 'T'), (i, j, 'R'))
                    union((i, j, 'B'), (i, j, 'L'))
        res = 0
        for e in p:
            if e == p[e]:
                res += 1
        return res