class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for elem in s:
            if stack and elem == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([elem,1])
        res = ""
        for a,b in stack:
            res += a*b
        return res