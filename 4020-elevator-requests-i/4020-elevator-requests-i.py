class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        res = 0
        cur_floor = 0
        for i in range(len(requests)):
            res += abs(requests[i] - cur_floor)
            cur_floor = requests[i]
        return res