class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # use Floyd-Washall -> O(n^3)
        dist = [[inf] * n for _ in range(n)]
        for a, b, w in edges:
            dist[a][a] = dist[b][b] = 0
            dist[a][b] = w
            dist[b][a] = w
        for k in range(n):
            for a in range(n):
                for b in range(n):
                    dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
        res = [0] * n
        for i in range(n):
            for j in range(n):
                if dist[i][j] <= distanceThreshold and i != j:
                    res[i] += 1
        ans = 0
        for i in range(n):
            if res[i] <= res[ans]:
                ans = i
        return ans