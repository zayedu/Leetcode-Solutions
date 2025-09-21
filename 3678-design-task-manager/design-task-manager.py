class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {} 
        self.priority = []
        for userId, taskId, priority in tasks:
            self.tasks[taskId] = (priority,userId)
            heapq.heappush(self.priority, (-priority,-taskId,userId))

        

        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (priority,userId)

        heapq.heappush(self.priority,(-priority,-taskId,userId))



    def edit(self, taskId: int, newPriority: int) -> None:
        userId= self.tasks[taskId][1]
        self.tasks[taskId] = (newPriority, userId)
        heapq.heappush(self.priority, (-newPriority, -taskId, userId))


    def rmv(self, taskId: int) -> None:
        if taskId in self.tasks:
            del self.tasks[taskId]
    
    def execTop(self) -> int:

        while self.priority :
            negP, negT, userId = heapq.heappop(self.priority)
            taskId = -negT
            priority = -negP
            cur = self.tasks.get(taskId)
            if cur is None or cur != (priority, userId):
                continue
            
            del self.tasks[taskId]
            return userId
        return -1





# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()