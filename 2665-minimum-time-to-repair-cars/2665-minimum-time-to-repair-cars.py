class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepair(time):
            n = cars
            for rank in ranks:
                n -= floor(sqrt(time/rank))
            return n <= 0
        l, r = 0, 100*cars*cars
        while l <= r:
            mid = (l+r)//2
            if canRepair(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l