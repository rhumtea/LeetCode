class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = []
        min_cost = inf
        for i in range(len(cost)):
            min_cost = min(min_cost, cost[i])
            res.append(min_cost)
        return res