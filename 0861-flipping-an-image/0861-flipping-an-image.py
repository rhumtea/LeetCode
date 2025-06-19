class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range((n+1)//2):
                print("a", i, j)
                print("b", i, n-1-j)
                temp = image[i][j]
                image[i][j] = image[i][n-1-j]
                image[i][n-1-j] = temp
                image[i][j] = 0 if image[i][j] else 1
                image[i][n-1-j] = 0 if image[i][n-1-j] else 1
            if n%2:
                image[i][n//2] = 0 if image[i][n//2] else 1 
        return image