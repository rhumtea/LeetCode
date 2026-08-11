class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = inf
        for task in tasks:
            res = min(res, task[0]+task[1])
        return res