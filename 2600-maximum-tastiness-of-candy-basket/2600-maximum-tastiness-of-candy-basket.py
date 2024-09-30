class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        a = list(price)
        a.sort()
        def check(mid):
            count = 1
            diff = a[0] + mid
            for i in range(1, len(a)):
                if a[i] >= diff:
                    diff = a[i] + mid
                    count += 1
            return count
        l, r = 0, 10**9
        res = 0
        while l <= r:
            mid = (l+r)//2
            if check(mid) >= k:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


