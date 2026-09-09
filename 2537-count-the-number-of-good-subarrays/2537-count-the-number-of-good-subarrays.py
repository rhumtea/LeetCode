class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        def count_pair(n):
            return n * (n-1) // 2
        w = defaultdict(int)
        pairs = 0
        res = 0
        l = 0
        for r in range(len(nums)):
            t = nums[r]
            pairs -= count_pair(w[t])
            w[t] += 1
            pairs += count_pair(w[t])
            while pairs >= k:
                res += len(nums) - r
                a = nums[l]
                pairs -= count_pair(w[a])
                w[a] -= 1
                pairs += count_pair(w[a])
                l += 1
        return res