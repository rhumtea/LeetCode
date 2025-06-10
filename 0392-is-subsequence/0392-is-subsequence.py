class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        elif t == "":
            return False
        i = j = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
        return False