class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs)):
            if strs[i].isdigit(): res = max(res, int(strs[i]))
            else: res = max(res, len(strs[i]))
        return res