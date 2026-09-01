class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        res = -1
        smallest = inf
        for i in range(len(drones)):
            t = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
            if t <= drones[i][2] and t < smallest:
                smallest = t
                res = i
        return res