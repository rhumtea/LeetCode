class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        worktime = {}
        worktime[logs[0][0]] = logs[0][1]
        for i in range(1, len(logs)):
            temp = logs[i][1] - logs[i-1][1]
            if logs[i][0] not in worktime:
                worktime[logs[i][0]] = temp
            else:
                worktime[logs[i][0]] = max(worktime[logs[i][0]], temp)
        key = list(worktime.keys())
        value = list(worktime.values())
        maxTime, smallID = 0, n
        for i in range(len(value)):
            if value[i] > maxTime:
                maxTime = value[i]
                smallID = key[i]
            elif value[i] == maxTime and key[i] < smallID:
                smallID = key[i]
        return smallID