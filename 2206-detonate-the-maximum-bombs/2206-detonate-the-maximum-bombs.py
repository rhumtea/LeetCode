class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                d = sqrt((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2)
                if d <= bombs[i][2]:
                    adj[i].append(j)
        res = 0
        def dfs(u):
            if u in visit:
                return
            visit.add(u)
            for v in adj[u]:
                dfs(v)
        for i in range(n):
            visit = set()
            dfs(i)
            res = max(res, len(visit))
        return res