class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for elem in s:
            if elem == '(':
                stack.append(elem)
            elif elem == ')' and (stack == [] or stack[-1] == ')'):
                stack.append(')')
            else:
                stack.pop()       
        return len(stack)