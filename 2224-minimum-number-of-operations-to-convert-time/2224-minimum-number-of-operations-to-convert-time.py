class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        timeCurrent =  int(current[:2]) * 60 + int(current[3:5])
        timeCorrect  = int(correct[:2]) * 60 + int(correct[3:5])
        diff = timeCorrect - timeCurrent
        print(diff)
        thislist = [60, 15, 5, 1]
        count = 0
        for i in thislist:
            count += diff // i
            diff %= i
        return count