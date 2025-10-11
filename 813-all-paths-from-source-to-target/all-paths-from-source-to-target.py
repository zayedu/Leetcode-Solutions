class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        def dfs(node, path):
            if node == n - 1:
                paths.append(list(path))
                return

            for child in graph[node]:
                path.append(child)
                dfs(child, path)
                path.pop()

        dfs(0, [0])
        return paths 