class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        graph1 = collections.defaultdict(list)
        graph2 = collections.defaultdict(list)

        for i, (a,b) in enumerate(pairs1):
            graph1[a].append((b, rates1[i]))
            graph1[b].append((a, 1/rates1[i]))

        for i, (a,b) in enumerate(pairs2):
            graph2[a].append((b, rates2[i]))
            graph2[b].append((a, 1/rates2[i]))
        
        def bfs(start, graph):
            best = collections.defaultdict(float)
            queue = collections.deque()
            queue.append((start, 1.0))
            visited = set()
            while queue:
                cur, val = queue.popleft()
                best[cur] = max(best[cur], val)
                visited.add(cur)
                for nei, mult in graph[cur]:
                    if nei not in visited:
                        queue.append((nei, val * mult))
            return best
        
        bestconversion1 = bfs(initialCurrency, graph1)
        bestconversion2 = bfs(initialCurrency, graph2)

        maxconversion = 0
        for currency in bestconversion1:
            if currency in bestconversion2:
                maxconversion = max(maxconversion, bestconversion1[currency] / bestconversion2[currency])
        
        return maxconversion
        