class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            w = succProb[i]
            adj[u].append([v, w])
            adj[v].append([u, w])
        pq = [[-1, start_node]]
        prob = [0] * n
        prob[start_node] = 1
        while pq:
            d, cur = heappop(pq)
            d = -d
            if prob[cur] > d: continue
            for ne, w in adj[cur]:
                if d * w > prob[ne]:
                    prob[ne] = d*w
                    heappush(pq, [-d*w, ne])
        return prob[end_node]
