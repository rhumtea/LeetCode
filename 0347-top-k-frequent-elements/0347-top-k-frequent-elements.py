class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        res = []
        count = 0
        for num in nums:
            mp[num] += 1
        pq = []
        for key,v in mp.items():
            heappush(pq, [-v, key])
        while pq:
            if count == k: break
            count += 1
            temp = heappop(pq)
            res.append(temp[1])
        return res