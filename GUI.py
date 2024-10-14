from tkinter import *
from tkinter import messagebox, simpledialog




#Main Window

main = Tk()
main.geometry("720x520")
main.title('Daily Planner')
menu = Menu(main)
main.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=main.quit)
#Variables


messages = []
selectedmessages = []
messagetexts = []
message_counter = 0
##

def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def marked(widget_index):
    global replacement
    global selectedmessages
    global changed
    if len(selectedmessages) < 2:
        # Mark the first widget to be swapped
        selectedmessages.append(widget_index)
        messages[widget_index].config(bg="lightgreen")  # Highlight the widget to indicate selection
    if len(selectedmessages) == 1:
        current_message = messagetexts[selectedmessages[0]]
        replacement = Text(main,height =5, width= 20)
        replacement.place(x=495,y=200)
        replacement.insert(END,current_message)
    if len(selectedmessages) == 2:
        switch_pos()
        replacement.destroy()
        current_message = None

# Function to swap positions of two widgets using pack()
def switch_pos():
    global selectedmessages
    global messages
    global messagetexts
    index1, index2 = selectedmessages

    messages[index1], messages[index2] = messages[index2], messages[index1]
    messagetexts[index1], messagetexts[index2] = messagetexts[index2], messagetexts[index1]
    for message in messages:
        message.pack_forget()

    for i,message in enumerate(messages):
        message.pack(pady=5)
        message.bind("<Button-1>", lambda event, b=i: marked(b))

    for message in messages:
        message.config(bg='SystemButtonFace')


    selectedmessages = []


def add_task():
    global messages, messagetexts

    #creating text for message
    message_text = f"Task {len(messagetexts) + 1}"
    #add_tasks(tasks,message_text)
    messagetexts.append(message_text)
    # Create the message widget
    message = Message(scrollable_frame, text=message_text, width=200,padx=10, pady=5,relief='solid')
    message.pack(pady=5)
    message.bind("<Button-1>", lambda event,b=len(messages):marked(b))
    # Update the canvas scroll region to account for the new message
    canvas.configure(scrollregion=canvas.bbox("all"))
    messages.append(message)

#Edit function
def edit_task():
    if len(selectedmessages) == 0:
        messagebox.showerror("No Task is selected", "Select a task that you wish to edit")
        return
    else:
        changed = replacement.get(1.0, "end-1c")
        target = messages[selectedmessages[0]]
        target.config(text=changed)
        messagetexts[selectedmessages[0]] = changed
        
def delete_task():
    global selectedmessages
    if len(selectedmessages) == 0:
        messagebox.showerror("No Task is selected", "Select a task that you wish to delete")
        return
    else:

        for message in messages:
            message.pack_forget()

        target = messages[selectedmessages[0]]
        target.destroy()
        numbertarget = messages.index(target)
        print(numbertarget)
        messagetexts.pop(numbertarget)
        messages.remove(target)
        
        for i,message in enumerate(messages):
            message.pack(pady=5)
            message.bind("<Button-1>", lambda event, b=i: marked(b))

    selectedmessages = []

def mark_task_as_done():
    global selectedmessages
    if len(selectedmessages) == 0:
        messagebox.showerror("No Task is selected", "Select a task that you wish to mark as done")
        return
    else:
        delete_task()
        messagebox.showinfo("Hooray","One less thing to worry about!")
#added buttons 



add_task_button = Button(main, text="Add New Task", command=add_task)
add_task_button.place(x=560,y=400)

edit_task_button = Button(main,text="Edit Task", command=edit_task)
edit_task_button.place(x=480,y=400)


delete_task_button = Button(main,text="Delete Task", command=delete_task)
delete_task_button.place(x=515,y=440)

Mark_task_done_button = Button(main,text="Mark Task As Done", command=mark_task_as_done)
Mark_task_done_button.place(x=500,y=360)
#Canvas and scrollbar
canvas = Canvas(main, height=600, width=400, borderwidth= 1, relief="solid")
scrollbar = Scrollbar(main, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to contain widgets
scrollable_frame = Frame(canvas)

# Update the canvas scroll region when the frame's size changes
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Add the scrollable frame to the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Bind mouse wheel event for scrolling
canvas.bind_all("<MouseWheel>", on_mouse_wheel)


canvas.place(x=0,y=0)
scrollbar.pack(side="right", fill="y")




#create tasks
















main.mainloop()
