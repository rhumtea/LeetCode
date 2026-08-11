class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = j = 0
        for i in range(len(g)):
            while j < len(s):
                if s[j] >= g[i]:
                    res += 1
                    j += 1
                    break
                j += 1
        return res
