class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        gain = [0] + gain
        prefix = [0] * len(gain)
        for i in range(1, len(gain)):
            prefix[i] = prefix[i-1] + gain[i]
            res = max(res, prefix[i])
        return res