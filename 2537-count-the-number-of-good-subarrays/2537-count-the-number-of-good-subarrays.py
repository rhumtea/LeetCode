class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        def count_pairs(x):
            return x * (x-1) // 2

        w = defaultdict(int)
        res = pairs = l = 0
        n = len(nums)
        for r in range(n):
            pairs -= count_pairs(w[nums[r]])
            w[nums[r]] += 1
            pairs += count_pairs(w[nums[r]])
            while pairs >= k:
                res += n - r
                pairs -= count_pairs(w[nums[l]])
                w[nums[l]] -= 1
                pairs += count_pairs(w[nums[l]])
                l += 1
        return res