from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        index of rains is day
        rains[index] is lake i.e ans[index]
        """


        ans = [1]*len(rains)
        rainy_days = {} #day/idx -> day it was filled
        sunny_days = SortedList()

        for index in range(len(rains)):
            if rains[index] == 0:
                sunny_days.add(index)
                continue

            if rains[index] in rainy_days:
                day_it_rained = rainy_days[rains[index]] #0
                next_sunny_day = sunny_days.bisect_right(day_it_rained) #1

                if next_sunny_day == len(sunny_days):
                     #no sunny day after it last rained i.e we cannot dry this lake before it rains again
                     return []
                
                ans[sunny_days[next_sunny_day]] = rains[index]
                sunny_days.pop(next_sunny_day)

            ans[index] = -1
            rainy_days[rains[index]] = index

        return ans
        '''
        rains = [1,2,0,0,2,1]
                           ^
        sunny_days = [ 3 ]
        rainy_day = { 
            1 : 0,
            2 : 4,
        }

        ans = [-1,-1,2,1,1,1]
        '''
                