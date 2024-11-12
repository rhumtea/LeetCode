class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        newSet = set();
        for i in nums:
            for j in range(i[0], i[1]+1):
                if j not in newSet: newSet.add(j)
        return len(newSet)
