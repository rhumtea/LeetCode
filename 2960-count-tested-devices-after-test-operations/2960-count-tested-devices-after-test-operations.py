class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        countTestedDevice = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > countTestedDevice:
                countTestedDevice += 1
        return countTestedDevice
        # countDevice = 0
        # for i in range(len(batteryPercentages)-1):
        #     if batteryPercentages[i] > 0:
        #         countDevice += 1
        #     batteryPercentages[i+1] = max(0, batteryPercentages[i+1] - countDevice)
        # if batteryPercentages[-1] > 0:
        #     countDevice += 1
        # return countDevice