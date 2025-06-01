class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        arr = [0] * 32
        i = 0
        while n > 0:
            d = n & 1
            arr[i] = d
            n >>= 1
            i += 1
        for i in range(len(arr)):
            res += arr[::-1][i] * 1 << i
        return res