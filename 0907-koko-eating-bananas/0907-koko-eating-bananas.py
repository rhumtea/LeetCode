class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            total = 0
            for p in piles:
                total += ceil(p/k)
            return total <= h
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r-l)//2
            if check(mid): r = mid-1
            else: l = mid+1
        return l
        
