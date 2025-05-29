class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = []
        lenght = len(nums)
        mp = defaultdict(int)
        for num in nums:
            for n in num:
                mp[n] += 1
        for k, v in mp.items():
            if v == lenght:
                res.append(k)
        res.sort()
        return res        