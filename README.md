# GroupProject-2

Repository for Software Engineering project #2 focusing on development of a To-Do-List
This repository was created for our second group project for CS 230 Software Engineering, meant to create a to-do list that enables you to load and save tasks in a file, add tasks, display the tasks, delete tasks, edit tasks, and mark tasks as completed. A password must be entered into the terminal before accessing the to-do list.

# Installation 

Download the files and open them in whatever code editor you prefer, or use git to clone the repository.
```bash
git clone https://github.com/Jlyon6984/GroupProject-2.git
```
To run the program, enter the desired password to access the commands to make changes to the to-do list. 

# Usage
Python

# Functions
```python
#Load tasks into Json file

load_tasks()

#Save tasks to Json file

save_Tasks()

#Clear all the tasks from the Json file

clear_Tasks()

#Add a task into the Json file

add_Task()

#Displays tasks written in the Json file

show_Tasks()

#Changes the status of a task(Complete, Incomplete, Inprogress, etc)

update_task_status()

#deletes a task from the Json file

delete_task()

#Access a certain task and make changes to it

edit_task()

#Creates a password needed to access the to-do list

verify_password()

#Creates a JSON file to act as another to-do list

add_list()

#changes which to-do list is accessed 

change_list()
```
# Further Documentation
All tasks are stored in JSON files, the first file accessed is tasks.json. More lists can be made with the creation of more JSON files.

Colorama was implemented into the program to add color to the text in the terminal. When completing an action, the result of that action will be written in green. If an action is not completed due to an invalid option or the status of the task is incomplete, the message will be written in red. 

## Contribution
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

Current Contributors: 
  David Headen, Jake Lyon, Wyatt Harris, Riker Sweazey


