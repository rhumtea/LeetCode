class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        res = [0] * n
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        def dijkstra(u):
            pq = [[0, u]]
            dist = [inf] * n
            dist[u] = 0
            while pq:
                d, cur = heappop(pq)
                if dist[cur] < d: continue
                for ne, w in adj[cur]:
                    if d + w < dist[ne]:
                        dist[ne] = d + w
                        heappush(pq, [d+w, ne])
            for i in range(n):
                if i != u and dist[i] <= distanceThreshold:
                    res[i] += 1
        for i in range(n):
            dijkstra(i)
        ans = 0
        for i in range(n):
            if res[i] <= res[ans]:
                ans = i
        return ans

        