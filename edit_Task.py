import json
def edit_task(tasks):
    if tasks:
        try:
            task_index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= task_index < len(tasks):
                new_task = input(f"Enter the new task description for Task {task_index + 1}: ")
                tasks[task_index]["task"] = new_task
                print(f"Task {task_index + 1} has been updated.")
                save_tasks(tasks)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")
    else:
        print("No tasks to edit.")
