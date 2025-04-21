class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        closing_parentheis = 0
        for elem in s:
            if elem == '(':
                stack.append(elem)
            elif elem == ')':
                if stack:
                    stack.pop()
                else:
                    closing_parentheis += 1
        return len(stack) + closing_parentheis