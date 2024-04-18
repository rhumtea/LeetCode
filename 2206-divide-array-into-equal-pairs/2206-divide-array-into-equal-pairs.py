class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # nums.sort()
        # count = 0
        # for i in range(0, len(nums), 2):
        #     if nums[i] != nums[i+1]:
        #         return False
        # return True
        thisdict = Counter(nums)
        for i in thisdict.values():
            if i % 2 != 0:
                return False
        return True
        