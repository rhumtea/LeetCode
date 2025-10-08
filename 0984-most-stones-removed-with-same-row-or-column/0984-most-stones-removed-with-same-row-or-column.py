class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        p = list(range(n))
        size = [1] * n
        R = [0] * n
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
        row, col = defaultdict(list), defaultdict(list)
        for i in range(len(stones)):
            a, b = stones[i]
            row[a].append(i)
            col[b].append(i)
            if row[a]:
                union(row[a][0], i)
            if col[b]:
                union(col[b][0], i)
        pa = set()
        for i in range(n):
            pa.add(find(i))
        return n - len(pa)