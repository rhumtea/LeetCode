class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(mid):
            num = cars
            for rank in ranks:
                num -= floor(sqrt(mid/rank))
            return num <= 0
        l, r = 1, 100 * cars * cars
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l