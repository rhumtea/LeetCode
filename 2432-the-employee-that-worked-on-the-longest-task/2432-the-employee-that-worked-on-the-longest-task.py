class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        maxTime = logs[0][1]
        smallID = logs[0][0]
        for i in range(1, len(logs)):
            temp = logs[i][1] - logs[i-1][1]
            if maxTime < temp:
                maxTime = temp
                smallID = logs[i][0]
            elif maxTime == temp:
                smallID = min(smallID, logs[i][0])
        return smallID