class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        total_cost = 0
        n = len(costs)
        costs.sort(key = lambda x:(x[0]-x[1]))

        for index in range(n):
            
            if index < n/2:
                total_cost += costs[index][0]
            else:
                total_cost += costs[index][1]

        return total_cost
        