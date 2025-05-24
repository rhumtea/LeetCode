class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.mp = defaultdict(int)
        self.mp[1] = big
        self.mp[2] = medium
        self.mp[3] = small

    def addCar(self, carType: int) -> bool:
        if self.mp[carType]:
            self.mp[carType] -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)