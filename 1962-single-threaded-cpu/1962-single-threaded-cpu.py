class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = []
        for i in range(len(tasks)):
            sorted_tasks.append([tasks[i][0], tasks[i][1], i])
        sorted_tasks = sorted(sorted_tasks, key=lambda x:x[0])

        res = []
        cur = 0
        waitlist = []
        N = len(sorted_tasks)
        i = 0
        while waitlist or i < N:
            if waitlist == [] and cur < sorted_tasks[i][0]:
                cur = sorted_tasks[i][0]
            while i < N and sorted_tasks[i][0] <= cur:
                heappush(waitlist, [sorted_tasks[i][1], sorted_tasks[i][2]])
                i += 1
            if waitlist:
                temp = heappop(waitlist)
                res.append(temp[1])
                cur += temp[0]
        return res