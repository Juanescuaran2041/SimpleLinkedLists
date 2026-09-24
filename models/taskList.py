from models.task import Task, Priority
from models.node_task import NodeTask


class TaskList:
    def __init__(self):
        self.first_task = None
        self.last_task = None
        self.task_count = 0

    def is_empty(self):
        return self.first_task is None

    def size(self):
        return self.task_count

    def addTask(self, task: Task):
        new_task = NodeTask(task)

        if self.first_task is None:
            self.first_task = new_task
            self.last_task = new_task
        else:
            self.last_task.next = new_task
            self.last_task = new_task

        self.task_count += 1

    def addTaskFirst(self, task: Task):
        new_task = NodeTask(task)
        new_task.next = self.first_task
        self.first_task = new_task

        if self.last_task is None:
            self.last_task = new_task

        self.task_count += 1

    def completeTask(self, title: str):
        taskCompleted = self.find_task(title)

        if taskCompleted is None:
            return False

        taskCompleted.task.complete_task()
        return True

    def removeTask(self, title: str):
        current = self.first_task
        previous = None

        while current is not None:
            if current.task.name == title:
                if previous is None:
                    self.first_task = current.next
                else:
                    previous.next = current.next
                if current == self.last_task:
                    self.last_task = previous
                self.task_count -= 1
                return True

            previous = current
            current = current.next

        return False

    def list_all(self):
        tasks = []
        current = self.first_task
        while current is not None:
            tasks.append(current.task)
            current = current.next

        return tasks

    def list_by_priority(self, priority: Priority):
        tasks = []
        current = self.first_task

        while current is not None:
            if current.task.priority == priority:
                tasks.append(current.task)
            current = current.next

        return tasks

    def list_pending(self):
        return [task for task in self.list_all() if not task.complete]

    def list_completed(self):
        return [task for task in self.list_all() if task.complete]

    def find_task(self, title: str):
        current = self.first_task

        while current is not None:
            if title == current.task.name:
                return current
            current = current.next

        return None

    def __str__(self):
        names = [task.name for task in self.list_all()]
        return " -> ".join(names + ["None"])
