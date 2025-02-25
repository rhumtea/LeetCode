class NumArray:

    def __init__(self, nums: List[int]):
        # self.nums = nums # This one is only ref to nums
        arr = nums
        self.arr = arr

    def sumRange(self, left: int, right: int) -> int:
        prefix = [0]
        for i in self.arr:
            prefix.append(prefix[-1] + i)
        return prefix[right+1] - prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)