class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        mp_r = defaultdict(int)
        mp_s = defaultdict(int)
        max_r = 0
        for i in range(len(ranks)):
            mp_r[ranks[i]] += 1
            mp_s[suits[i]] += 1
            max_r = max(max_r, mp_r[ranks[i]])
        if len(mp_s) == 1:
            return "Flush"
        elif max_r >= 3:
            return "Three of a Kind"
        elif max_r == 2:
            return "Pair"
        else:
            return "High Card"