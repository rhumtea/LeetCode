class Solution:
    def countDigits(self, num: int) -> int:
        newNum, count = num, 0
        while newNum != 0:
            digit = newNum % 10
            if num % digit == 0:
                count += 1
            newNum //= 10
        return count