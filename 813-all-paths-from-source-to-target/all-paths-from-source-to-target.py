
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        seen = set()

        def dfs(node,path):
            if node == len(graph)-1:
                paths.append(path)
                return

            if node in seen:
                return

            seen.add(node)

            for edge in graph[node]:
                path.append(edge)
                dfs(edge,path.copy())
                path.pop()
            seen.remove(node)

        dfs(0,[0])

        return paths

