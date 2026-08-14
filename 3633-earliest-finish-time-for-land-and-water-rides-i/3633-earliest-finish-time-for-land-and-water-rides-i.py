class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_land_end = inf
        for i in range(len(landStartTime)):
            min_land_end = min(min_land_end, landStartTime[i] + landDuration[i])
            
        min_water_end = inf
        for i in range(len(waterStartTime)):
            min_water_end = min(min_water_end, waterStartTime[i] + waterDuration[i])
            
        land_water = inf
        for i in range(len(waterStartTime)):
            finish_time = max(min_land_end, waterStartTime[i]) + waterDuration[i]
            land_water = min(land_water, finish_time)
            
        water_land = inf
        for i in range(len(landStartTime)):
            finish_time = max(min_water_end, landStartTime[i]) + landDuration[i]
            water_land = min(water_land, finish_time)
            
        return min(land_water, water_land)