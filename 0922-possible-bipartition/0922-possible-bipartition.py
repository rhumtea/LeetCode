class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[b].append(a)
            adj[a].append(b)
        visit = [0] * (n+1)
        visit[0] = 1
        print(adj)
        def dfs(cur, p):
            if visit[cur] == 0:
                visit[cur] = 3 - visit[p]
            else:    
                if visit[cur] == visit[p]:
                    return False 
                else:
                    return True
            for ne in adj[cur]:
                if ne != p:
                    if not dfs(ne, cur):
                        return False
            return True
        for i in range(1, len(visit)):
            if visit[i] == 0:
                if dfs(i, 0) == False:
                    return False
        return True