class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        L, R = 0, len(string_x)-1
        while L <= R:
            if string_x[L] != string_x[R]:
                return False
            else:
                L += 1
                R -= 1
        return True