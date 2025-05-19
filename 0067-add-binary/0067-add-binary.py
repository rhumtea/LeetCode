class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        cout = i = j = 0
        a = a[::-1]
        b = b[::-1]
        while i < len(a) or j < len(b) or cout:
            temp = 0
            temp += cout
            if i < len(a):
                temp += int(a[i])
                i += 1
            if j < len(b):
                temp += int(b[j])
                j += 1
            res.append(str(temp % 2))
            cout = temp // 2
        return ''.join(res[::-1])