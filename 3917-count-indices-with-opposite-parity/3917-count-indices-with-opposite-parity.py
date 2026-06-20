class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd = even = 0
        for num in nums:
            if num % 2 == 0: even += 1
            else: odd += 1
        odd_count = even_count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = odd - odd_count
                even_count += 1
            else:
                nums[i] = even - even_count
                odd_count += 1
        return nums
            