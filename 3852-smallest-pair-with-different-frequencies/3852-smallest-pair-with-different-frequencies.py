class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = defaultdict(int)
        x = inf
        for i in range(len(nums)):
            freq[nums[i]] += 1
            x = min(x, nums[i])
        y = inf
        for k, v in freq.items():
            if k > x and v != freq[x] and k < y:
                y = k
        return [x, y] if (x != y and y != inf) else [-1,-1]