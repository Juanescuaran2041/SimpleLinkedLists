from models.task import Task, Priority
from models.taskList import TaskList


def print_tasks(title, tasks):
    print(f"\n--- {title} ({len(tasks)}) ---")
    for task in tasks:
        print(" ", task)


def main():
    task_list = TaskList()
    print("¿Lista vacía al iniciar?", task_list.is_empty())

    task_list.addTask(Task("Estudiar", "Repasar listas enlazadas", "2026-09-25", Priority.HIGH))
    task_list.addTask(Task("Compras", "Comprar mercado", "2026-09-26", Priority.LOW))
    task_list.addTask(Task("Proyecto", "Avanzar proyecto de software", "2026-09-27", Priority.MEDIUM))
    task_list.addTask(Task("Gimnasio", "Rutina de piernas", "2026-09-28", Priority.LOW))
    task_list.addTaskFirst(Task("Parcial", "Presentar parcial de cálculo", "2026-09-24", Priority.HIGH))

    print("\nEstructura:", task_list)
    print("Tamaño:", task_list.size())
    print_tasks("Todas las tareas", task_list.list_all())
    print_tasks("Prioridad ALTA", task_list.list_by_priority(Priority.HIGH))
    print_tasks("Prioridad BAJA", task_list.list_by_priority(Priority.LOW))

    print("\nCompletar 'Estudiar':", task_list.completeTask("Estudiar"))
    print("Completar 'Inexistente':", task_list.completeTask("Inexistente"))
    print_tasks("Completadas", task_list.list_completed())
    print_tasks("Pendientes", task_list.list_pending())

    node = task_list.find_task("Proyecto")
    print("\nBuscar 'Proyecto':", node.task if node else "No encontrada")

    print("\nEliminar primera ('Parcial'):", task_list.removeTask("Parcial"))
    print("Eliminar del medio ('Compras'):", task_list.removeTask("Compras"))
    print("Eliminar última ('Gimnasio'):", task_list.removeTask("Gimnasio"))
    print("Eliminar inexistente:", task_list.removeTask("Nada"))
    print("Estructura:", task_list)
    print("Última tarea:", task_list.last_task.task.name)

    # Verificaciones automáticas
    assert task_list.size() == 2
    assert [t.name for t in task_list.list_all()] == ["Estudiar", "Proyecto"]
    assert task_list.first_task.task.name == "Estudiar"
    assert task_list.last_task.task.name == "Proyecto"
    assert task_list.find_task("Estudiar").task.complete

    task_list.removeTask("Estudiar")
    task_list.removeTask("Proyecto")
    assert task_list.is_empty() and task_list.last_task is None
    assert task_list.removeTask("Algo") is False
    print("\n Todas las pruebas pasaron")


if __name__ == "__main__":
    main()
