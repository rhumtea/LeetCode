class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            temp = str(i)
            for j in temp:
                res.append(int(j))
        return res