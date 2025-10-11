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
        seen_d1 = set()

        def dfs(node,units):
            max_day_1[node] = max(max_day_1[node],units)

            if node in seen_d1:
                return

            seen_d1.add(node)

            for edge,rate in adj_list_1[node]:
                dfs(edge,units*rate)

            seen_d1.remove(node)


        dfs(initialCurrency,1)
        max_units = max_day_1[initialCurrency]
        seen_d2 = set()
        def dfs_2(node,units):
            if node == initialCurrency:
                nonlocal max_units
                max_units = max(units,max_units)
                return

            if node in seen_d2:
                return
            
            seen_d2.add(node)
            for edge,rate in adj_list_2[node]:
                dfs_2(edge,units*rate)

            seen_d2.remove(node)
            
                
        for node, units in max_day_1.items():
            dfs_2(node,units)
            
        return(max_units)