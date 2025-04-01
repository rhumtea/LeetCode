class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        def helper(arr):
            product = 1
            for i in arr: product = product * i % mod
            return product
        
        pq = []
        for num in nums: heappush(pq, num)
        res = helper(pq)
        # k(log(n))
        while k != 0:
            temp = heappop(pq)+1
            heappush(pq, temp)
            k -= 1
        return helper(pq)
        
