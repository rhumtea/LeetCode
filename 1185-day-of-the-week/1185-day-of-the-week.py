class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        #use dict for store days of week, days of month
        # Monday = 1/1/1 -> 1 is Monday
        dayOfWeek = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 0:"Sunday"}
        dayOfMonth = {1:31, 
                      2:29 if year%4 == 0 and (year%400 == 0 or year%100 != 0) else 28,
                      3:31, 4:30, 5:31, 6:30, 7:31, 8:31,9:30, 10:31, 11:30, 12:31}
        #count day before given year
        #leap year if divisible by 4 except for years evenly divisible by 100 but not by 400
        daysBefore = 365*(year-1) + (year-1)//4 - (year-1)//100 + (year-1)//400
        #count day in given year
        daysGivenYear = 0    
        for i in range(1, month):
            daysGivenYear += dayOfMonth[i]
        daysGivenYear += day
        #total day to given day
        totalDays = daysBefore + daysGivenYear
        return dayOfWeek[totalDays%7]
        

        