class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        checkBulky, checkHeavy = False, False
        volume = length * width * height
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9:
            checkBulky = True
        if mass >= 100:
            checkHeavy = True
        if checkBulky == checkHeavy:
            if checkBulky == True: return "Both"
            else: return "Neither"
        else:
            if checkBulky == True: return "Bulky"
            else: return "Heavy"