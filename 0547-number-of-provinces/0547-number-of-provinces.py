class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [False] * N
        res = 0
        pq = deque()
        for si in range(N):
            if not visited[si]:
                res += 1
                pq.append(si)
                visited[si] = True
            while pq:
                i  = pq.popleft()
                for j in range(N):
                    if isConnected[i][j] == 1 and not visited[j]:
                        pq.append(j)
                        visited[j] = True
        return res