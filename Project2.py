import json
import os
from colorama import Fore, Back, Style, init


# Load tasks from file
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Clears tasks in file
def clear_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump([], file)
        
# Add a task
def add_task(tasks):
    print(Style.RESET_ALL)
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(Fore.GREEN + "Task added!")
    save_tasks(tasks)

# Show all tasks
def show_tasks(tasks):
    if tasks:
        print(Style.BRIGHT + "\nTasks:")
        for index, task in enumerate(tasks):
            status = Fore.GREEN + "Done" if task["done"] else Fore.RED + "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")
    else:
        print(Fore.YELLOW + "No tasks to show.")
        # print(Style.RESET_ALL)
        
# Mark a task as done
def mark_task_done(tasks):
    if tasks:
        try:
            task_index = int(input(Style.BRIGHT + "Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print(Fore.GREEN + f"Task {task_index + 1} marked as done!")
                save_tasks(tasks)
            else:
                print(Fore.RED + "Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")
    else:
        print(Style.DIM + Fore.YELLOW + "No tasks to mark as done.")
        

# Delete a task
def delete_task(tasks):
    if tasks:
        try:
            delInput = input(Style.BRIGHT + "Enter the task number to delete (or type 'all' to clear all tasks): ")
            if delInput == "all":
                clear_tasks(tasks)
                tasks.clear()  # Have to clear the memory of it cuz its WEIRD
                print(Fore.GREEN + "All tasks cleared!")
                return
            task_index = int(delInput) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(Fore.GREEN + f"Task '{deleted_task['task']}' deleted!")
                save_tasks(tasks)
            else:
                print(Fore.RED + "Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")
    else:

        print(Style.DIM + Fore.YELLOW + "No tasks to delete.")
       
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
        
# Password verification
def verify_password(stored_password):
    attempts = 3
    while attempts > 0:
        password = input("Enter the password: ")
        if password == stored_password:
            print("Access granted!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. You have {attempts} attempt(s) left.")
    print("Access denied!")
    return False

    
# Main function
def main():
    stored_password = "pass1"  # going to hash this for more security after break
    if verify_password(stored_password):
        tasks = load_tasks()
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Style.RESET_ALL)
    init(autoreset=True)

    tasks = load_tasks()

    while True:
        # print(Style.RESET_ALL)
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Mark Task as Done")
        print("6. Exit")
        
        choice = input(Style.DIM + "Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            mark_task_done(tasks)
        elif choice == "6":
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")
        print(Style.RESET_ALL)

   
    
if __name__ == "__main__":
    main()
            
