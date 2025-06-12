class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        mp = defaultdict(int)
        for i in range(1, len(nums)+1):
            mp[i] += 1
            mp[nums[i-1]] -= 1
        for k, v in mp.items():
            if v > 0:
                res.append(k)
        return res