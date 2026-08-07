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
                    ans = abs(v[i]-v[i+1]) + abs(v[i]-v[i+2]) + abs(v[i+1]-v[i+2])
                    res = min(res, ans)
        return res if res != inf else -1