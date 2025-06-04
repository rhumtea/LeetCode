class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 3:
            n_str = str(n)
            n = 0
            for i in range(len(n_str)):
                n += int(n_str[i]) ** 2
            if n == 4:
                return False
        return True if n == 1 else False