class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        destination_node = len(graph)-1
        adjacency_list = { }

        for index in range(len(graph)):
            adjacency_list[index] = graph[index]  
            
        all_paths = []

        
        def dfs(node):

            if node == destination_node:
                all_paths.append(path.copy())

            for edge in adjacency_list[node]:
                path.append(edge)
                dfs(edge)
                path.pop()
        path = [0]
        dfs(0)
        return all_paths    