class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            str_i = str(i)
            if len(str_i)%2 != 0: continue
            mid = len(str_i)//2
            leftSum = sum(map(int, str_i[:mid]))
            rightSum = sum(map(int, str_i[mid:]))
            if leftSum == rightSum: count += 1
        return count
            
