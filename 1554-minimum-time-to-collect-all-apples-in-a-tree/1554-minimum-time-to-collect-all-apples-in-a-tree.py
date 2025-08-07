class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(cur, p):
            res = 0
            for ne in adj[cur]:
                if ne != p:
                    t = dfs(ne, cur)
                    if t > 0 or hasApple[ne]:
                        res += t + 2
            return res
        return dfs(0, -1)