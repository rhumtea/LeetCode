class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #use Binary Search and use 2D matrix as 1D matrix
        numOfRow = len(matrix)
        numOfColumn = len(matrix[0])
        first = 0
        last = numOfRow * numOfColumn - 1
        while first <= last:
            midIndex = (first + last) // 2
            if matrix[midIndex // numOfColumn][midIndex % numOfColumn] == target:
                return True
            elif matrix[midIndex // numOfColumn][midIndex % numOfColumn] < target:
                first = midIndex + 1
            else:
                last = last - 1
        return False
