class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        res = ""
        if a > 0: heappush(pq, [-a, 'a'])
        if b > 0: heappush(pq, [-b, 'b'])
        if c > 0: heappush(pq, [-c, 'c'])
        while pq:
            x1, y1 = heappop(pq)
            if len(res) >= 2 and res[-1] == res[-2] == y1:
                if not pq: break
                x2, y2 = heappop(pq)
                res += y2
                if x2+1 < 0: heappush(pq, [x2+1, y2])
                heappush(pq, [x1,y1])
            else:
                res += y1
                if x1+1 < 0: heappush(pq, [x1+1,y1])
        return res