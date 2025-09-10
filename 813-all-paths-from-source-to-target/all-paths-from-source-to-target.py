class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        connections = {

        }

        '''
        connections should look like:
            node -> [connected_node1,...,connected_node_n]

        '''
        all_possible_paths = [ ]
        last_node = len(graph)
        for node in range(last_node):
            connections[node] = graph[node]

        def dfs(current_node, path):
            if current_node == last_node-1:
                all_possible_paths.append(path)
                
            else:
                for edge in connections[current_node]:
                    path.append(edge)
                    dfs(edge, list(path))
                    path.pop()

        dfs(0,[0])

        return all_possible_paths


