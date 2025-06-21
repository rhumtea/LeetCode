class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(mid):
            prev = position[0]
            count = 1
            for i in range(1, len(position)):
                if position[i] - prev >= mid:
                    count += 1
                    prev = position[i]
            return count >= m
        position.sort()
        l, r = 1, position[-1] 
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l-1