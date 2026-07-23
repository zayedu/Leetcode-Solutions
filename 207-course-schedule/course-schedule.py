from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        adj_list = defaultdict(list)
        in_deg = [0] * numCourses

        for pre,crs in prerequisites:
            adj_list[pre].append(crs)
            in_deg[crs] += 1

        queue = deque()
        for course in range(numCourses):
            if in_deg[course] == 0:
                queue.append(course)

        count = 0
        while queue:
            leaf = queue.popleft()
            count += 1
            for edge in adj_list[leaf]:
                in_deg[edge] -= 1
                if in_deg[edge] == 0:
                    queue.append(edge)

        return count == numCourses