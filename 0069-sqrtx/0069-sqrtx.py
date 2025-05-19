class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, 2**31 - 1
        while L <= R:
            mid = L + (R - L) // 2
            if (mid * mid <= x):
                L = mid + 1
            else:
                R = mid - 1
        return R