class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        mp = defaultdict(int)
        while n > 0:
            t = n % 10
            mp[t] += 1
            n //= 10
        min_freq = inf
        res = inf
        for k, v in mp.items():
            if v < min_freq:
                min_freq = v
                res = k
            elif v == min_freq:
                res = min(res, k)
        return res