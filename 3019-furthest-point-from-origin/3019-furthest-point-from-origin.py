class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        mp = defaultdict(int)
        for move in moves:
            mp[move] += 1

        return abs(mp['L'] - mp['R']) + mp['_']