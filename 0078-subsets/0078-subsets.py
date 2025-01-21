class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        for n in range(0, 1<<N):
            temp = []
            for i in range(n):
                if (n&(1<<i))>0: temp.append(nums[i])
            res.append(temp)
        return res