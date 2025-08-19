class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        dq_p = deque()
        dq_a = deque()
        pacific = set()
        atlantic = set()
        for si in range(M):
            for sj in range(N):
                if si == 0 or sj == 0:
                    pacific.add((si, sj))
                    dq_p.append((si, sj))
                if si == M-1 or sj == N-1:
                    atlantic.add((si, sj))
                    dq_a.append((si, sj))
        while dq_p:
            for _ in range(len(dq_p)):
                i, j = dq_p.popleft()
                for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in pacific and heights[ni][nj] >= heights[i][j]:
                        pacific.add((ni, nj))
                        dq_p.append((ni, nj))
        while dq_a:
            for _ in range(len(dq_a)):
                i, j = dq_a.popleft()
                for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in atlantic and heights[ni][nj] >= heights[i][j]:
                        atlantic.add((ni, nj))
                        dq_a.append((ni, nj))
        return list(pacific & atlantic)