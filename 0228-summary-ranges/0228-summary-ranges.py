class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums: return res
        temp = nums[0]
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] != nums[i-1]+1:
                if temp == nums[i-1]: res.append(str(temp))
                else: res.append(f"{temp}->{nums[i-1]}")
                if i < len(nums): temp = nums[i]
        return res
                
        return res