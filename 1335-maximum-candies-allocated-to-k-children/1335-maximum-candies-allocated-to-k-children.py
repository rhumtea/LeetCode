class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid):
            summ = 0
            for candy in candies:
                summ += candy // mid
            return summ >= k
        l, r = 1, max(candies)
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
