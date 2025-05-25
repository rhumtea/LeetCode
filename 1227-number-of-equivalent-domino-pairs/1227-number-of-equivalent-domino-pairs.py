class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        mp = defaultdict(int)
        for domino in dominoes:
            temp = (domino[0], domino[1]) if domino[0] < domino[1] else (domino[1], domino[0])
            res += mp[temp]
            mp[temp] += 1
        return res