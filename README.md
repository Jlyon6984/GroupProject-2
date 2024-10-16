# GroupProject-2

Repository for Software Engineering project #2 focusing on development of a To-Do-List
This repository was created for our second group project for CS 230, Software Engineering meant to create a to-do List, that enables you to load and save tasks in a file, add tasks, display the tasks, delete tasks, edit tasks, and mark tasks as completed. A password must be entered into the terminal before accessing the to-do list.

# Installation 

Download the files and open them in whatever code editor you prefer, or use git to clone the repository.

git clone https://github.com/Jlyon6984/GroupProject-2.git

# Usage
Python

# Functions

#Load tasks into Json file

load_Tasks()

#Save tasks to Json file

save_Tasks()

#Clear all the tasks from the Json file

clear_Tasks()

#Add a task into the Json file

add_Task()

#Displays tasks written in the Json file

show_Tasks()

#Mark tasks in the Json file as completed

mark_task_done()

#deletes a task from the Json file

delete_task()

#Access a certain task and make changes to it

edit_task()

#Creates a password needed to access the to-do list

verify_password()

# Further Documentation
All tasks are stored in a Json file called tasks.json.

Colorama was implemented into the program to add color to the text in the terminal. When completing an action, the result of that action will be written in green. If an action is not completed due to an invalid option or the status of the task is incomplete, the message will be written in red. 

## Contribution
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

Current Contributors: 
  David Headen, Jake Lyon, Wyatt Harris, Riker Sweasley


