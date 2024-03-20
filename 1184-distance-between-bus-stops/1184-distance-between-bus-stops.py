class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if (start > destination):
            temp = destination
            destination = start
            start = temp
        countClockwise = sum(distance[start:destination])
        countCounterClockwise = sum(distance[destination:]) + sum(distance[:start])
        return min(countClockwise,countCounterClockwise)
            