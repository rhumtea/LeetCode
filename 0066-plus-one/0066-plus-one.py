class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] + out <= 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                continue
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
