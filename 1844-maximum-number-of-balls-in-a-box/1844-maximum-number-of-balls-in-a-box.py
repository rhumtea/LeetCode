class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def helper(num):
            num_str = str(num)
            summ = 0
            for num in num_str:
                summ += int(num)
            return summ
        res = 0
        mp = defaultdict(int)
        for num in range(lowLimit, highLimit + 1):
            temp = helper(num)
            mp[temp] += 1
            res = max(res, mp[temp])
        return res