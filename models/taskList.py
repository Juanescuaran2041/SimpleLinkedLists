from task import Task, Priority
from node_task import NodeTask


class TaskList:
    def __init__(self):
        self.first_task = None
        self.last_task = None
        self.task_count = 0

    def addTask(self, task:Task):
        new_task = NodeTask(task)

        if self.first_task is None:
            self.first_task = new_task
            self.last_task = new_task
        else:
            self.last_task.next = new_task
            self.last_task = new_task

        self.task_count += 1

    def completeTask(self, title:str):
        taskCompleted = self.find_task(title)

        if taskCompleted is None:
            return False
        else:
            taskCompleted.task.complete

        return True

    def removeTask(self, title:str):
        current = self.first_task
        previous = None

        while current.next is not None:
            if current.task.name == title:
                if previous is None:
                    self.first_task = current.next
                else:
                    previous.next = current.next
                if current == self.last_task:
                    self.last_task = previous
                self.task_count -=1
                return True
            
            previous = current
            current = current.next

        return False

    def list_all(self):
        tasks = []
        current = self.first_task
        while current is not None:
            tasks.append(current)

            current = current.next
        
        return tasks

    def list_by_priority (self, priority:Priority):
        tasks = []
        current = self.first_task
        
        while current is not None:
            if current.task.priority == priority:
                tasks.append(current)
            current = current.next

        return tasks


    def find_task(self, title:str):
        current = self.first_task

        while current is not None:
            if (title == current.task.name):
                return current
            current = current.next

        return None
        