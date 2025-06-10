class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heappush(pq, (-a, 'a'))
        if b > 0:
            heappush(pq, (-b, 'b'))
        if c > 0:
            heappush(pq, (-c, 'c'))
        res = ""
        while pq:
            temp = heappop(pq)
            if len(res) >= 2 and res[-1] == res[-2] == temp[1]:
                if not pq:
                    break
                temp1 = heappop(pq)
                res += temp1[1]
                if temp1[0]+1 < 0:
                    heappush(pq, (temp1[0]+1, temp1[1]))
                heappush(pq, (temp[0], temp[1]))
            else:
                res += temp[1]
                if temp[0]+1 < 0:
                    heappush(pq, (temp[0]+1, temp[1]))
        return res