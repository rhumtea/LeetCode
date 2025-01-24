class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = 0
        for i in range(len(nums)):
            res ^= (i+1)
            res ^= nums[i]
        temp = res
        position = 0
        while temp > 0:
            if temp&1 == 0: position += 1
            else: break
            temp >>= 1
        temp = 0
        for i in range(len(nums)):
            if (i+1)&(1<<position)>0: temp ^= (i+1)
            if nums[i]&(1<<position)>0: temp ^= nums[i]
        return [temp, res^temp] if temp in nums else [res^temp, temp]


         