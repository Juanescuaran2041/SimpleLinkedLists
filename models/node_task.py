from task import Task

class NodeTask:
    def __init__(self, task:Task):
        self.task = task
        self.next = None


    