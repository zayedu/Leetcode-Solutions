import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}

        '''
        task_id -> [user_id,priority]
        '''
        self.heap = []
        
        for user,task,priority in tasks:
            heapq.heappush(self.heap, (-1*priority,-1*task))
            self.tasks[task] = [user,priority]
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = [userId, priority]
        heapq.heappush(self.heap,(-1*priority,-1*taskId))


    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks[taskId][1] = newPriority
        heapq.heappush(self.heap,(-newPriority,-taskId))
        

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]
        

    def execTop(self) -> int:
        
        while self.heap:
            priority,task_id = heapq.heappop(self.heap)
            priority *= -1
            task_id *= -1

            if task_id in self.tasks and priority == self.tasks[task_id][1]:
                user_id = self.tasks[task_id][0]
                del self.tasks[task_id]
                return user_id





        return -1



# obj.edit(taskId,newPriority)
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.rmv(taskId)
# param_4 = obj.execTop()