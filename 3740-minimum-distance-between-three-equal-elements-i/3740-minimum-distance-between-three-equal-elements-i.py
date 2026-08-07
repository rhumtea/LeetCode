class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index = defaultdict(list)
        for i in range(len(nums)):
            index[nums[i]].append(i)
        res = inf
        print(index)
        for v in index.values():
            if len(v) >= 3:
                for i in range(len(v)-2):
                    #ans = v[i+1] - v[i] + v[i+2] - v[i] + v[i+2] - v[i+1]
                    #ans = 2 * (v[i+2] - v[i])
                    ans = 2 * (v[i+2] - v[i])
                    res = min(res, ans)
        return res if res != inf else -1