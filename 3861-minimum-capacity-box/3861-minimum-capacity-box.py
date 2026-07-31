class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        smallest = 101
        index = -1
        for i in range(len(capacity)):
            if capacity[i] >= itemSize and smallest > capacity[i]:
                smallest = capacity[i]
                index = i
        return index