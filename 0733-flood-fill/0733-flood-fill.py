class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        pq = [(sr, sc)]
        c = image[sr][sc]
        M, N = len(image), len(image[0])
        while len(pq) >= 1:
            i, j = heappop(pq)
            image[i][j] = color
            if (i, j) not in visited:
                visited.add((i,j))
                for dx, dy in dir:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < M and 0 <= nj < N and image[ni][nj] == c:
                        heappush(pq, (ni,nj))
        return image