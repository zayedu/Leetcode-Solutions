class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x:x[0]-x[1])
        n = len(costs)/2
        cost = 0
        for index in range(len(costs)):
            if index < n:
                cost += costs[index][0]
            else:
                cost += costs[index][1]

        return cost
