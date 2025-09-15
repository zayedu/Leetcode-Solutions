class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_to_pre = {i:[] for i in range(numCourses)}


        for prerequisite in prerequisites:
            if prerequisite[0] in course_to_pre:
                course_to_pre[prerequisite[0]].append(prerequisite[1])
            else:
                course_to_pre[prerequisite[0]]= [prerequisite[1]]

        seen = set()

        def dfs(course):

            if course in seen:
                return False
            if course_to_pre[course] == []:
                return True
            seen.add(course)

            for prereq in course_to_pre[course]:
                if not dfs(prereq):
                    return False

            seen.remove(course)
            course_to_pre[course] = []
            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        