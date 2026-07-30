class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        res = defaultdict(int)
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                res[nums[i]] += 1
        for k, v in res.items():
            if v == 1:
                return k
        return -1