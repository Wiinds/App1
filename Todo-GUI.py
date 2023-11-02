from Modules import Todo_Functions
import PySimpleGUI as PySGUI 

label = PySGUI.Text("Type in a To-Do")
input_box = PySGUI.InputText(tooltip="Enter To-do", key="Todo")

add_button = PySGUI.Button("Add")


Window = PySGUI.Window('My To-Do App', 
                       layout=[[label],[input_box, add_button]], 
                       font=("Helvetica", 15))

while True:
    Event, Values = Window.read()

    match Event:
        case "Add":
            todos = Todo_Functions.get_todos()
            new_todo = Values['Todo'] + "\n"
            todos.append(new_todo)
            Todo_Functions.write_todos(todos)
        case PySGUI.WIN_CLOSED:
            break   
            

Window.close()



