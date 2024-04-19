class Solution:
    def digitSum(self, s: str, k: int) -> str:
        res = s
        while len(res) > k:
            res = [int(i) for i in res]
            temp = ""
            for i in range(0, len(res), k):
                temp += str(sum(res[i:i+k]))
            res = temp
        return res
