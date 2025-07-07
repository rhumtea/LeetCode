class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(cur):
            visit.add(cur)
            for ne in adj[cur]:
                if ne == destination:
                    return True
                if ne not in visit:
                    if dfs(ne):
                        return True
            return False
        return dfs(source)
        