class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(cur):
            if cur == destination:
                return True
            if cur in visit:
                return False
            visit.add(cur)
            for ne in adj[cur]:
                if dfs(ne):
                    return True
            return False
        return dfs(source)