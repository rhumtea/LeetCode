class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        oddList = [nums[i] for i in range(len(nums)) if i%2 == 1]
        evenList = [nums[i] for i in range(len(nums)) if i%2 == 0]
        oddList.sort(reverse=True)
        evenList.sort()
        res = []
        for i in range(len(oddList)):
            res.append(evenList[i])
            res.append(oddList[i])
        if len(evenList) > len(oddList):
            res.append(evenList[-1])
        return res
            