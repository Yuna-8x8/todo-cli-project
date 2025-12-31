if choice == "1":
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added successfully.")
def add_task(todo_list):
    task = input("Enter task: ")
    todo_list.append(task)
    print("Task added successfully")
