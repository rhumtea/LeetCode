class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            check = numbers[left] + numbers[right]
            if check == target:
                return [left+1, right+1]
            elif check > target:
                right -= 1
            else:
                left += 1