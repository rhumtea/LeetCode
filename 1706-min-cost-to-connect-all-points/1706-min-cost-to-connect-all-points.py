class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        arr = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a, b = points[i]
                c, d = points[j]
                w = abs(a-c) + abs(b-d)
                arr.append([w, i, j])
        arr.sort()
        n = len(points)
        p = list(range(n))
        size = [1] * n
        def find(u):
            while u != p[u]:
                u = p[u]
            return u
        def union(u,v):
            u, v = find(u), find(v)
            if u == v:
                return False
            p[v] = u
            size[u] += size[v]
            return True
        res = 0
        for w, a, b in arr:
            if find(a) != find(b):
                union(a, b)
                res += w
        return res