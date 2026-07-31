class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on_bulbs = set()
        for i in range(len(bulbs)):
            if bulbs[i] in on_bulbs:
                on_bulbs.remove(bulbs[i])
            else:
                on_bulbs.add(bulbs[i])
        return sorted(on_bulbs)