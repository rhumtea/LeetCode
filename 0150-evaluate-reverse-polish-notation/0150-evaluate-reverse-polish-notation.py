class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper(token, a, b):
            if token == '+':
                return a + b
            elif token == '-':
                return a - b
            elif token == '*':
                return a * b
            else:
                if a*b < 0:
                    return -(abs(a)//abs(b))
                else:
                    return a//b
        stack = []
        for token in tokens:
            if token in "+-*/":
                temp = stack.pop()
                temp1 = stack.pop()
                stack.append(helper(token, temp1, temp))
            else:
                stack.append(int(token))
        return stack[0]