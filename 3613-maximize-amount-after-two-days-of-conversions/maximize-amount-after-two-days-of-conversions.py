class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        adj_list_1 = defaultdict(list)
        adj_list_2 = defaultdict(list)
        for index in range(len(pairs1)):
            adj_list_1[pairs1[index][0]].append([pairs1[index][1],rates1[index]])
            adj_list_1[pairs1[index][1]].append([pairs1[index][0],1/rates1[index]])
        for index in range(len(pairs2)):
            adj_list_2[pairs2[index][0]].append([pairs2[index][1],rates2[index]])
            adj_list_2[pairs2[index][1]].append([pairs2[index][0],1/rates2[index]])

        max_day_1 = defaultdict(float)
        max_day_1[initialCurrency] = 1.0


        queue=[(initialCurrency,1.0)]
        while queue:
            node,units = queue.pop()
            if units < max_day_1[node]:
                continue
            max_day_1[node] = max(units,max_day_1[node])


            for edge,rate in adj_list_1[node]:
                if units*rate > max_day_1[edge]:
                    queue.append((edge,units*rate))

            
        queue = list(max_day_1.items())

        max_day_2 = defaultdict(float)

        while queue:
            node,units = queue.pop()
            
            if units < max_day_2[node]:
                continue
            max_day_2[node] = units

            for edge, rate in adj_list_2[node]:
                if rate*units > max_day_2[edge]:
                    
                    queue.append((edge,units*rate))

        return max(max_day_2[initialCurrency],max_day_1[initialCurrency])