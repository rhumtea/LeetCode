class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return float(sqrt(num)) == int(sqrt(num))