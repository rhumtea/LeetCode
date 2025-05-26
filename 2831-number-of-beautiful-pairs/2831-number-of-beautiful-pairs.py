class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def helper(x,y):
            while y:
                x, y = y, x%y
            return x
        res = 0
        for i in range(len(nums)):
            temp = int(str(nums[i])[0])
            for j in range(i+1, len(nums)):
                temp1 = int(str(nums[j])[-1])
                if helper(temp, temp1 ) == 1:
                    res += 1
        return res 