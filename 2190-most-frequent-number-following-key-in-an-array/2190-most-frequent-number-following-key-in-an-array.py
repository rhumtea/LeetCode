class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        thisdict = {}
        for i in range(len(nums) - 1):
            if nums[i] == key and nums[i+1] not in thisdict:
                thisdict[nums[i+1]] = 1
            elif nums[i] == key and nums[i+1] in thisdict:
                thisdict[nums[i+1]] += 1
        return max(zip(thisdict.values(), thisdict.keys()))[1]
