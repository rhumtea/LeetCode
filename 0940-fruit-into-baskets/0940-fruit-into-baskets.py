class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        l = 0
        w = defaultdict(int)
        for r in range(len(fruits)):
            w[fruits[r]] += 1
            while len(w) > 2:
                w[fruits[l]] -= 1
                if w[fruits[l]] == 0: del w[fruits[l]]
                l += 1
            res = max(res, r-l+1)
        return res