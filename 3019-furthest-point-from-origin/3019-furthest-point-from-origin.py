class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count_ = 0
        res = 0
        for i in range(len(moves)):
            if moves[i] == 'L': res += 1
            elif moves[i] == 'R': res -= 1
            else: count_ +=1
        return abs(res) + count_
            