class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        sorted_strs = sorted(strs)
        n = len(sorted_strs[0])
        for i in range(n):
            if sorted_strs[0][i] == sorted_strs[-1][i]:
                res += sorted_strs[0][i]
            else:
                break
        return res
        
