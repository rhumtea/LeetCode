class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = inf
        for i in range(len(landStartTime)):
            a = landStartTime[i]
            b = landDuration[i]
            for j in range(len(waterStartTime)):
                e = waterStartTime[j]
                f = waterDuration[j]
                res = min(res, max(a + b, e) + f, max(e + f, a) + b)
        return res