class MyCalendar:

    def __init__(self):
        self.sl = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.sl:
            self.sl.add([startTime, endTime])
            return True
        index = bisect_right(self.sl, [startTime, endTime])
        if index-1 >= 0 and startTime < self.sl[index-1][1]:
            return False
        if index < len(self.sl) and endTime > self.sl[index][0]:
            return False
        self.sl.add([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)