def view_tasks(todo_list):
    print("Your Tasks:")
    for i in range(len(todo_list)):
        print(i, todo_list)   # ❌ BUG: prints full list repeatedly

