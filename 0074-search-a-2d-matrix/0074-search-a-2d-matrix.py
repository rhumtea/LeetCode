class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #iterate through rows
        for row in range(len(matrix)):
            #iterarte through column
            for col in range(len(matrix[0])):
                if  matrix[row][col] == target:
                    return True
        return False