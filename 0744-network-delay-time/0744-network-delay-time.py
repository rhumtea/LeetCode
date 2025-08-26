class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append([v, w])
        dist = [inf] * (n+1)
        pq = [[0, k]]
        dist[k] = 0
        while pq:
            d, cur = heappop(pq)
            if dist[cur] < d: continue
            for ne, w in adj[cur]:
                if d + w < dist[ne]:
                    dist[ne] = d + w
                    heappush(pq, [d+w, ne])
        res = max(dist[1:])
        return res if res < inf else -1