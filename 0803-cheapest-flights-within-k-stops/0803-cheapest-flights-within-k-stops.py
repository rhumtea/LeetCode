class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append([w, v])
        step = 0
        dist = [inf] * n
        q = deque([[0, src]])
        dist[src] = 0
        while q and step < k + 1:
            for _ in range(len(q)):
                d, cur = q.popleft()
                for nw, ne in adj[cur]:
                    if d + nw < dist[ne]:
                        q.append([d+nw, ne])
                        dist[ne] = d + nw
            step += 1
        return dist[dst] if dist[dst] < inf else -1