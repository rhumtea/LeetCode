class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new_tasks = []
        for i in range(len(tasks)):
            new_tasks.append((tasks[i][0], tasks[i][1], i))
        new_tasks.sort(key=lambda x:x[0])
        res = []
        pq = []
        current_time = i = 0
        n = len(new_tasks)
        while pq or i < n:
            if pq == [] and current_time < new_tasks[i][0]:
                current_time = new_tasks[i][0]
            while i < n and new_tasks[i][0] <= current_time:
                heappush(pq, (new_tasks[i][1], new_tasks[i][2]))
                i += 1
            if pq:
                enqueue_time, index = heappop(pq)
                res.append(index)
                current_time += enqueue_time
        return res