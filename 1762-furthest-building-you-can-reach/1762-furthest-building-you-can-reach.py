class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        n = len(heights)
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0: continue
            if ladders: 
                ladders -= 1
                heappush(pq, diff)
            else:
                heappush(pq, diff)
                bricks -= heappop(pq)
                if bricks < 0: return i
        return n-1
        