class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals or len(intervals) <= 1:
            return intervals
        result = [intervals[0]]
        for item in intervals[1:]:
            if item[0] <= result[-1][1]:
                result[-1][1]=max(result[-1][1], item[1])
            else:
                result.append(item)
        return result