class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(u):
            if u == destination:
                return True
            if u in visit:
                return False
            visit.add(u)
            for v in adj[u]:
                if dfs(v):
                    return True
            return False
        return dfs(source)
        