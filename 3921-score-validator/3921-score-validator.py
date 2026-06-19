class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        total = 0
        counter = 0
        for event in events:
            if counter == 10: return [total, counter]
            if event in ["0","1","2","3", "4", "6"]: total += int(event[0])
            elif event in ["WD", "NB"]: total += 1
            elif event == "W": counter += 1
        return [total, counter]