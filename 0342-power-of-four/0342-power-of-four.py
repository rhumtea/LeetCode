class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            if int(sqrt(n)) * int(sqrt(n)) == n and n & (n-1) == 0:
                return True
        return False