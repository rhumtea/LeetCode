class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApple = sum(apple)
        if totalApple > sum(capacity):
            return len(capacity)
        capacity.sort(reverse=True)
        for i in range(len(capacity)):
            totalApple -= capacity[i]
            if totalApple <= 0:
                return i+1

        