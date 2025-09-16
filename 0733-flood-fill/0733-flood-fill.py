class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        srcColor = image[sr][sc]
        M, N = len(image), len(image[0])
        visit = [[False] * N for _ in range(M)]
        def dfs(i, j):
            image[i][j] = color
            visit[i][j] = True
            for ni, nj in [[i+1,j], [i-1, j], [i,j+1], [i, j-1]]:
                if 0 <= ni < M and 0 <= nj < N and image[ni][nj] == srcColor and visit[ni][nj] == False:
                    dfs(ni, nj)
        dfs(sr, sc)
        return image