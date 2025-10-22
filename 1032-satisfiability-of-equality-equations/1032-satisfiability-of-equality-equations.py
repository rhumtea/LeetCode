class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = 26
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
        notequal = []
        for e in equations:
            if e[1] == "=":
                a = ord(e[0]) - ord('a')
                b = ord(e[3]) - ord('a')
                union(a, b)
            else:
                notequal.append(e)
        for e in notequal:
            a = ord(e[0]) - ord('a')
            b = ord(e[3]) - ord('a')
            if find(a) == find(b):
                return False
        return True