from Modules import Todo_Functions
import PySimpleGUI as PySGUI 
import time

PySGUI.theme("Black")

#clock, title, input. and list box
clock = PySGUI.Text("", key="clock")
label = PySGUI.Text("Type in a To-Do")
input_box = PySGUI.InputText(tooltip="Enter To-do", key="Todo")
list_box = PySGUI.Listbox(values=Todo_Functions.get_todos(), key="Todos", 
                          enable_events=True, size=[45, 10])
#buttons
add_button = PySGUI.Button("Add")
edit_button = PySGUI.Button("Edit")
complete_button = PySGUI.Button("Complete")
exit_button = PySGUI.Button("Exit")
#Window layout
Window = PySGUI.Window('My To-Do App', 
                       layout=[[clock],
                               [label],
                               [input_box, add_button], 
                               [list_box, edit_button, complete_button],
                               [exit_button]], 
                       font=("Helvetica", 15))

while True:
    Event, Values = Window.read(timeout=500)
    Window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    #print(Event)
    #print(Values)
    #print(Values["Todos"])
    match Event:
        case "Add":
            todos = Todo_Functions.get_todos()
            new_todo = Values['Todo'] + "\n"
            todos.append(new_todo)
            Todo_Functions.write_todos(todos)
            Window["Todos"].update(values=todos)
            Window["Todo"].update(value="")
        case "Edit":
            try:
                edit_todo = Values["Todos"][0]
                new_todo = Values['Todo']
                todos = Todo_Functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                Todo_Functions.write_todos(todos)
                Window["Todos"].update(values=todos)
            except IndexError:
                PySGUI.popup("Please select a item first", font=("Helvetica", 15))    
        case "Complete":
            try:
                completed_todo = Values["Todos"][0]
                todos = Todo_Functions.get_todos()
                todos.remove(completed_todo)
                Todo_Functions.write_todos(todos)
                Window["Todos"].update(values=todos)
                Window["Todo"].update(value="")
            except IndexError:
                PySGUI.popup("Please select a item first", font=("Helvetica", 15))    
        case "Exit":
            break
        case "Todos":
            Window["Todo"].update(value=Values["Todos"][0])
        case PySGUI.WIN_CLOSED:
            break   

Window.close()



