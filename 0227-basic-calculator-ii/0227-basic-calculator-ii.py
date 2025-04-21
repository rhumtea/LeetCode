class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        s = s.split(' ')
        s = ''.join(s)
        while i < len(s):
            if s[i].isdigit() or s[i] == '-':
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j += 1
                a = int(s[i:j])
                i = j
                stack.append(a)
            elif s[i] == '*':
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j += 1
                a = int(s[i+1:j])
                i = j
                b = stack.pop()
                stack.append(a*b)
            elif s[i] == '/':
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j += 1
                a = int(s[i+1:j])
                i = j
                b = stack.pop()
                if a*b<0:
                    stack.append(-(abs(b)//abs(a)))
                else:
                    stack.append(b//a)
            else:
                i += 1
        return sum(stack)