class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        res = 0
        max_freq = 0
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
            if mp[num] > max_freq:
                max_freq = mp[num]
                res = max_freq
            elif mp[num] == max_freq:
                res += max_freq
        return res