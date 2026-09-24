from enum import Enum


class Priority(Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1


class Task:
    def __init__(self, name, description, date, priority: Priority):
        self.name = name
        self.description = description
        self.date = date
        self.priority = priority
        self.complete = False

    def complete_task(self):
        self.complete = True

    def __str__(self):
        status = "✔" if self.complete else "✘"
        return f"[{status}] {self.name} ({self.priority.name}) - {self.date}: {self.description}"
