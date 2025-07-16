class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        restricted_set = set()
        for r in restricted:
            restricted_set.add(r)
        visit = set()
        def dfs(u):
            if u in restricted_set or u in visit:
                return
            visit.add(u)
            for v in adj[u]:
                dfs(v)
        dfs(0)
        return len(visit)