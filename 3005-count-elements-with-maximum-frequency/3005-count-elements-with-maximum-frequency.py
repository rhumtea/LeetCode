class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        thisdict = Counter(nums)
        maxFreq = 0
        res = 0
        for i in thisdict.values():
            if i > maxFreq:
                maxFreq = i
                res = i
            elif i == maxFreq:
                res += maxFreq
        return res