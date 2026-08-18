class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = []
        min_cost = inf
        for i in range(len(cost)):
            if min_cost > cost[i]:
                res.append(cost[i])
            else:
                res.append(min_cost)
            min_cost = min(min_cost, cost[i])
        return res