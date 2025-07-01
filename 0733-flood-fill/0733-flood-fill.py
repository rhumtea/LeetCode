class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        visit = [[False] * N for _ in range(M)]
        check = image[sr][sc]
        def dfs(i, j):
            visit[i][j] = True
            if image[i][j] == check:
                image[i][j] = color
            else:
                return
            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if  0 <= ni < M and 0 <= nj < N and visit[ni][nj] == False:
                    dfs(ni, nj)
        dfs(sr, sc)
        return image