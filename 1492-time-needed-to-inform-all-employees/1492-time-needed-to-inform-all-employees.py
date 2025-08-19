class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] == -1:
                continue
            adj[manager[i]].append(i)
        res = 0
        def dfs(cur, p):
            time = 0
            for ne in adj[cur]:
                t = dfs(ne, cur)
                time = max(time, t)
            return time + informTime[cur]
        return dfs(headID, -1)