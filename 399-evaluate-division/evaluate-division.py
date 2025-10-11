class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = defaultdict(list)

        for index in range(len(equations)):
            adj_list[equations[index][0]].append([equations[index][1],values[index]])
            adj_list[equations[index][1]].append([equations[index][0],1/values[index]])

        seen = set()

        def dfs(dividend,divisor):
            print(dividend,divisor)
            if dividend in seen:
                return -1

            edges = adj_list[dividend]

            for denominator,value in edges:
                
                if denominator == divisor:
                    return value

                seen.add(dividend)
                v = dfs(denominator,divisor)
                seen.remove(dividend)
                if v >= 0:
                    return value * v

            return -1


        ans = []

        for query in queries:
            ans.append(dfs(query[0],query[1]))

        return ans



        


