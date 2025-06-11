class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, 2**31 - 1
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid >= num:
                r = mid - 1
            else:
                l = mid + 1
        return l * l == num