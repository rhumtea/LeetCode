class Solution:
    def digitCount(self, num: str) -> bool:
        thisdict = Counter(num)
        res = True
        for i in range(len(num)):
            if int(num[i]) != thisdict[str(i)]:
                res = False
        return res