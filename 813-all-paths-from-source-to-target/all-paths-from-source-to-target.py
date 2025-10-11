class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph)-1
        visited = set()
        paths = []

        def dfs(node,path):
            
            if node == target:
                path.append(target)
                paths.append(path)

                return

            if node in visited:
                return

            path.append(node)
            visited.add(node)

            for edge in graph[node]:
                dfs(edge,list(path))

            visited.remove(node)
            path.pop()

        dfs(0,[])

        return paths