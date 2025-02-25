class NumArray:

    def __init__(self, nums: List[int]):
        # self.nums = nums # This one is only ref to nums
        # prefix only runs one time with init.
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        self.prefix = prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)