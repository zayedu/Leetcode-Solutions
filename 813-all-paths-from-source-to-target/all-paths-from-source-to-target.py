class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        end_node = len(graph)-1

        paths = []

        seen = set()

        def dfs(node, path):

            if node == end_node:

                paths.append(path.copy())
                return

            if node in seen:
                return

            seen.add(node)


            for edge in graph[node]:
                path.append(edge)
                dfs(edge,path)
                path.pop()

            seen.remove(node)



        dfs(0,[0])
        return paths


