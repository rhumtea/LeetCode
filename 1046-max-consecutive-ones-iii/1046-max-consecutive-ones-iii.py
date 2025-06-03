class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        w = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            w[nums[r]] += 1
            while w[0] > k:
                w[nums[l]] -= 1
                l += 1
            max_length = max(max_length, r-l+1)
        return max_length