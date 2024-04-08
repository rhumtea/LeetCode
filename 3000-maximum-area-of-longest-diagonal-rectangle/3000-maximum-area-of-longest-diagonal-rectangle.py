class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxArea = 0
        maxDiagonal = 0
        for i in range(len(dimensions)):
            newDiagonal = math.sqrt(dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1]) 
            if newDiagonal > maxDiagonal:
                maxDiagonal = newDiagonal
                maxArea = dimensions[i][0] * dimensions[i][1]
            elif newDiagonal == maxDiagonal and maxArea < dimensions[i][0] * dimensions[i][1]: 
                maxArea = dimensions[i][0] * dimensions[i][1]
        return maxArea
