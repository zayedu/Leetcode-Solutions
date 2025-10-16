from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        ans = [1]*len(rains)
        sunny_days = SortedList()#index of sunny days
        rainy_days = {} #lake(rains[i]) -> day it rained

        #rains[i] lake getting rained on on ith day

        for day in range(len(rains)):
            if rains[day] == 0:
                sunny_days.add(day)
                continue
            
            if rains[day] in rainy_days:
                day_it_rained = rainy_days[rains[day]]
                next_sunny_day = sunny_days.bisect_right(day_it_rained)

                if next_sunny_day == len(sunny_days):
                    return []
                
                ans[sunny_days[next_sunny_day]] = rains[day]
                sunny_days.pop(next_sunny_day)

            ans[day] = -1
            rainy_days[rains[day]] = day

        return ans
            