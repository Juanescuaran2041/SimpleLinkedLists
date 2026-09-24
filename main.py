import tkinter as tk
from tkinter import messagebox

from models.task import Task, Priority
from models.taskList import TaskList

task_list = TaskList()


def show_tasks(tasks):
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, str(task))
    count_label.config(text="Tasks: " + str(task_list.size()))


def add_task():
    name = name_entry.get().strip()
    if name == "":
        messagebox.showwarning("Warning", "The name is required")
        return
    if task_list.find_task(name) is not None:
        messagebox.showwarning("Warning", "A task with that name already exists")
        return

    task = Task(name, description_entry.get(), date_entry.get(), Priority[priority_var.get()])
    task_list.addTask(task)

    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    show_tasks(task_list.list_all())


def complete_task():
    title = title_entry.get().strip()
    if task_list.completeTask(title):
        messagebox.showinfo("Complete", "Task completed")
    else:
        messagebox.showerror("Error", "Task not found")
    show_tasks(task_list.list_all())


def remove_task():
    title = title_entry.get().strip()
    if task_list.removeTask(title):
        messagebox.showinfo("Remove", "Task removed")
    else:
        messagebox.showerror("Error", "Task not found")
    show_tasks(task_list.list_all())


def find_task():
    title = title_entry.get().strip()
    node = task_list.find_task(title)
    if node is None:
        messagebox.showerror("Error", "Task not found")
    else:
        messagebox.showinfo("Found", str(node.task))


def filter_by_priority():
    show_tasks(task_list.list_by_priority(Priority[filter_var.get()]))


window = tk.Tk()
window.title("Task List")

# Form to add a task
form = tk.LabelFrame(window, text="New task")
form.pack(fill="x", padx=10, pady=5)

tk.Label(form, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form, width=30)
name_entry.grid(row=0, column=1)

tk.Label(form, text="Description:").grid(row=1, column=0, sticky="w")
description_entry = tk.Entry(form, width=30)
description_entry.grid(row=1, column=1)

tk.Label(form, text="Date:").grid(row=2, column=0, sticky="w")
date_entry = tk.Entry(form, width=30)
date_entry.grid(row=2, column=1)

tk.Label(form, text="Priority:").grid(row=3, column=0, sticky="w")
priority_var = tk.StringVar(value="MEDIUM")
tk.OptionMenu(form, priority_var, "HIGH", "MEDIUM", "LOW").grid(row=3, column=1, sticky="w")

tk.Button(form, text="Add task", command=add_task).grid(row=4, column=1, sticky="w", pady=5)

# Operations by title
actions = tk.LabelFrame(window, text="Operations")
actions.pack(fill="x", padx=10, pady=5)

tk.Label(actions, text="Title:").grid(row=0, column=0)
title_entry = tk.Entry(actions, width=25)
title_entry.grid(row=0, column=1, columnspan=3)

tk.Button(actions, text="Complete", command=complete_task).grid(row=1, column=1, pady=5)
tk.Button(actions, text="Remove", command=remove_task).grid(row=1, column=2)
tk.Button(actions, text="Find", command=find_task).grid(row=1, column=3)

# Lists
lists = tk.LabelFrame(window, text="Tasks")
lists.pack(fill="both", expand=True, padx=10, pady=5)

buttons = tk.Frame(lists)
buttons.pack(fill="x")
tk.Button(buttons, text="All", command=lambda: show_tasks(task_list.list_all())).pack(side="left")
tk.Button(buttons, text="Pending", command=lambda: show_tasks(task_list.list_pending())).pack(side="left")
tk.Button(buttons, text="Completed", command=lambda: show_tasks(task_list.list_completed())).pack(side="left")

filter_var = tk.StringVar(value="HIGH")
tk.Button(buttons, text="By priority", command=filter_by_priority).pack(side="right")
tk.OptionMenu(buttons, filter_var, "HIGH", "MEDIUM", "LOW").pack(side="right")

listbox = tk.Listbox(lists, width=70, height=10)
listbox.pack(fill="both", expand=True, pady=5)

count_label = tk.Label(lists, text="Tasks: 0")
count_label.pack(anchor="w")

window.mainloop()
