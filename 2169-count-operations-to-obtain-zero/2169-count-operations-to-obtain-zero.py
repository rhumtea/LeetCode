class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # operation = 0
        # while num1 != 0 and num2 != 0:
        #     if num1 >= num2:
        #         num1 -= num2
        #     else:
        #         num2 -= num1
        #     operation += 1
        # return operation
        operation = 0
        while num2:
            operation += num1 // num2
            num1, num2 = num2, num1%num2
        return operation