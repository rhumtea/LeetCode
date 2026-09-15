class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for i in  range(len(fruits)):
            for  j in range(len(baskets)):
                if   fruits[i]    <= baskets[j]:
                    baskets[j] = 0
                    res   += 1
                    break
        return  len(fruits) - res