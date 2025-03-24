class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        count = res = 0
        for num in nums:
            heappush(pq, -num)
        while pq:
            res = heappop(pq)
            res = -res
            count += 1
            if count == k: return res
        return 0