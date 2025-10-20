class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj_list = defaultdict(list)

        for index in range(len(equations)):
            equation = equations[index]
            value = values[index]

            adj_list[equation[0]].append([equation[1],value])
            adj_list[equation[1]].append([equation[0],1/value])

        seen = set()
        def dfs(num,den):

            if num not in adj_list:
                return -1.0

            seen.add(num)
            ans = -1.0
            for edge,value in adj_list[num]:
                if edge == den:
                    ans = value

                if edge not in seen:
                    v = dfs(edge,den)

                    if v != -1.0:
                        ans = v*value

            seen.remove(num)

            return ans
        ans = []
        for query in queries:

            ans.append(dfs(query[0],query[1]))

        return ans

                




