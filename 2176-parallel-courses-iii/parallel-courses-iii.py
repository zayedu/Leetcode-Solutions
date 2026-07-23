from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], times: List[int]) -> int:

        # pre req -> crs

        adj_list = defaultdict(list)

        in_deg = [0]*n

        for pre,crs in relations:
            adj_list[pre].append(crs)
            in_deg[crs-1] +=1

        queue = deque()

        for index in range(len(in_deg)):
            if in_deg[index] == 0:
                queue.append(index+1)
                
        completion_time = list(times)
        while queue:
            node = queue.popleft()

            for edge in adj_list[node]:
                completion_time[edge - 1] = max(
                    completion_time[edge - 1],
                    completion_time[node - 1] + times[edge - 1]
                )

                in_deg[edge - 1] -= 1

                if in_deg[edge - 1] == 0:
                    queue.append(edge)

        return max(completion_time)

        
