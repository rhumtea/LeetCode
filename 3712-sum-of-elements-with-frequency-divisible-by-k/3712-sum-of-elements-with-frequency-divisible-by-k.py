class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        res = 0
        for key, value in freq.items():
            if value % k == 0:
                res += key * value
        return res