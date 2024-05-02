class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        if time[3] == "?": res *= 6
        if time[4] == "?": res *= 10
        if time[0:2] == "??":
            res *= 24
        elif time[0] == "?" and time[1] != "?":
            res *= 2 if time[1] in "456789" else 3
        elif time[1] == "?" and time[0] != "?":
            res *= 10 if time[0] in "01" else 4
        return res
