class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mpCuisines = defaultdict(lambda: SortedList())
        self.mpFoods = defaultdict(list)
        for i in range(len(foods)):
            self.mpCuisines[cuisines[i]].add([-ratings[i], foods[i]])
            self.mpFoods[foods[i]] = [cuisines[i], ratings[i]]

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.mpFoods[food]
        self.mpFoods[food] = [c, newRating]
        self.mpCuisines[c].remove([-r, food])
        self.mpCuisines[c].add([-newRating, food])
        

    def highestRated(self, cuisine: str) -> str:
        return self.mpCuisines[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)