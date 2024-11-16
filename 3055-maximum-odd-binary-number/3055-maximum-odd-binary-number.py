class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count= s.count('1') 
        numOfZero = len(s) - count
        return '1' * (count-1) + '0' * numOfZero + '1'

