class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while len(nums) > 1:
            flag = True
            min_sum = inf
            index = -1
            for i in range(len(nums)-1):
                temp = nums[i] + nums[i+1]
                if nums[i] > nums[i+1]: flag = False
                if temp < min_sum:
                    min_sum = temp
                    index = i
            if flag: break
            count += 1
            nums[index] = min_sum
            nums.pop(index+1)
        return count