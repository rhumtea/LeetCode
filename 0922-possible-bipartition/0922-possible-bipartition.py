class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        p = list(range(n+1))
        R = [0] * (n+1)
        size = [1] * (n+1)
        def find(u):
            while u != p[u]:
                u = p[u]
            return u
        def union (u, v):
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
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
            if adj[b]:
                union(a, adj[b][0])
            if adj[a]:
                union(b, adj[a][0])
        for a, b in dislikes:
            if find(a) == find(b):
                return False
        return True