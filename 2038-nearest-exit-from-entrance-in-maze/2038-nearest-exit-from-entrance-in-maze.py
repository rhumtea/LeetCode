class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        visit = [[False] * N for _ in range(M)]
        q = deque()
        a, b = entrance[0], entrance[1]  
        visit[a][b] = True
        q.append([a, b])
        step = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if (i == 0 or j == 0 or i == M - 1 or j == N - 1) and (i != a or j != b):
                    return step 
                for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= ni < M and 0 <= nj < N and visit[ni][nj] == False and maze[ni][nj] == '.':
                        q.append([ni, nj])
                        visit[ni][nj] = True
            step += 1
        return -1 