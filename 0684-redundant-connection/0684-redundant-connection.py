class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(n+1))
        size = [1] * (n+1)
        R = [0] * (n+1)
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
        for a, b in edges:
            if find(a) == find(b):
                return [a,b]
            else:
                union(a, b)