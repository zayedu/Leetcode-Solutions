from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        sunny_days = SortedList()
        full_lakes = {} #lake(idx) -> day filled

        for index in range(len(rains)):
            if rains[index] == 0:
                sunny_days.add(index)
                continue
            
            if rains[index] in full_lakes:

                next_sunny_day = sunny_days.bisect_right(full_lakes[rains[index]])
                if next_sunny_day == len(sunny_days):
                    return []
                dry_day = sunny_days[next_sunny_day]
                ans[dry_day] = rains[index]
                sunny_days.remove(dry_day)


            ans[index] =-1
            full_lakes[rains[index]] = index 

        return ans