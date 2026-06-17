class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq = defaultdict(int)
        res = []
        for i in nums:
            freq[i] += 1
            if freq[i] <= k:
                res.append(i)
        return res