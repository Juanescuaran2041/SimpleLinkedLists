from models.task import Task, Priority
from models.taskList import TaskList


def print_tasks(title, tasks):
    print(f"\n--- {title} ({len(tasks)}) ---")
    for task in tasks:
        print(" ", task)


def main():
    task_list = TaskList()
    print("Is the list empty at start?", task_list.is_empty())

    task_list.addTask(Task("Study", "Review linked lists", "2026-09-25", Priority.HIGH))
    task_list.addTask(Task("Groceries", "Buy groceries", "2026-09-26", Priority.LOW))
    task_list.addTask(Task("Project", "Work on the software project", "2026-09-27", Priority.MEDIUM))
    task_list.addTask(Task("Gym", "Leg day workout", "2026-09-28", Priority.LOW))
    task_list.addTaskFirst(Task("Exam", "Take the calculus exam", "2026-09-24", Priority.HIGH))

    print("\nStructure:", task_list)
    print("Size:", task_list.size())
    print_tasks("All tasks", task_list.list_all())
    print_tasks("HIGH priority", task_list.list_by_priority(Priority.HIGH))
    print_tasks("LOW priority", task_list.list_by_priority(Priority.LOW))

    print("\nComplete 'Study':", task_list.completeTask("Study"))
    print("Complete 'Missing':", task_list.completeTask("Missing"))
    print_tasks("Completed", task_list.list_completed())
    print_tasks("Pending", task_list.list_pending())

    node = task_list.find_task("Project")
    print("\nFind 'Project':", node.task if node else "Not found")

    print("\nRemove first ('Exam'):", task_list.removeTask("Exam"))
    print("Remove middle ('Groceries'):", task_list.removeTask("Groceries"))
    print("Remove last ('Gym'):", task_list.removeTask("Gym"))
    print("Remove missing:", task_list.removeTask("Nothing"))
    print("Structure:", task_list)
    print("Last task:", task_list.last_task.task.name)

    # Automatic checks
    assert task_list.size() == 2
    assert [t.name for t in task_list.list_all()] == ["Study", "Project"]
    assert task_list.first_task.task.name == "Study"
    assert task_list.last_task.task.name == "Project"
    assert task_list.find_task("Study").task.complete

    task_list.removeTask("Study")
    task_list.removeTask("Project")
    assert task_list.is_empty() and task_list.last_task is None
    assert task_list.removeTask("Anything") is False
    print("\n✅ All tests passed")


if __name__ == "__main__":
    main()
