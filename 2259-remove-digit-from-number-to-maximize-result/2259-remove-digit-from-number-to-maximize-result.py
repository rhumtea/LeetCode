class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []
        for i in range(len(number)):
            temp = number
            if number[i] == digit:
                temp = temp[:i] + temp[i+1:]
                res.append(int(temp))
        return str(max(res))