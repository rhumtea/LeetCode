class SmallestInfiniteSet:

    def __init__(self):
        self.pq = [1]
        self.saved_set = set()
        
    def popSmallest(self) -> int:
        temp = heappop(self.pq)
        if len(self.pq) == 0:
            heappush(self.pq, temp+1)
        self.saved_set.add(temp)
        return temp

    def addBack(self, num: int) -> None:
        if num in self.saved_set:
            heappush(self.pq, num)
            self.saved_set.remove(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)