class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        uppercase = "ABCDEFGHIJKLMNOPQRSTWXYUVZ"
        lowercase = "abcdefghijklmnopqrstwxyuvz"
        special = "!@#$%^&*()-+"
        digit = "0123456789"
        a, b, c, d = False, False, False, False
        if len(password) < 8: return False
        for i in range(len(password)):
            if password[i] in uppercase: a = True
            elif password[i] in lowercase: b = True
            elif password[i] in special: c = True
            elif password[i] in digit: d = True
            if i == len(password)-1:
                continue
            elif i != len(password)-1 and password[i] == password[i+1]: 
                return False
        return a == b == c == d == True
