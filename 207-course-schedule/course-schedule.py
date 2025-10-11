class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])

        visited = set()

        def dfs(node):

            if not adj_list[node]:
                return True

            if node in visited:
                return False

            visited.add(node)

            for edge in adj_list[node]:
                if not dfs(edge):
                    return False
                
            adj_list[node] = []
            visited.remove(node)
                
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

