class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        connections = { }

        for i in range(len(graph)):
            connections[i] = graph[i]

        last_node = len(graph)
        all_paths = [ ]

        def dfs(current_node, path):

            if current_node == last_node-1:
                all_paths.append(path)

            else:
                for edge in connections[current_node]:

                    path.append(edge)
                    dfs(edge,list(path))
                    path.pop()

                
        dfs(0,[0])

        return all_paths