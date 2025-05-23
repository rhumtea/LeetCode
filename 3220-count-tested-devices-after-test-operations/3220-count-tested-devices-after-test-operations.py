class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        for b in batteryPercentages:
            b = max(b-count, 0)
            if b > 0:
                count += 1
        return count