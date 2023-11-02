from Modules import Todo_Functions
import PySimpleGUI as PySGUI 

label = PySGUI.Text("Type in a To-Do")
input_box = PySGUI.InputText(tooltip="Enter To-do", key="Todo")

list_box = PySGUI.Listbox(values=Todo_Functions.get_todos(), key="Todos", 
                          enable_events=True, size=[45, 10])


add_button = PySGUI.Button("Add")

edit_button = PySGUI.Button("Edit")


Window = PySGUI.Window('My To-Do App', 
                       layout=[[label],[input_box, add_button], [list_box, edit_button]], 
                       font=("Helvetica", 15))

while True:
    Event, Values = Window.read()
    print(Event)
    print(Values)
    print(Values["Todos"])

    match Event:
        case "Add":
            todos = Todo_Functions.get_todos()
            new_todo = Values['Todo'] + "\n"
            todos.append(new_todo)
            Window["Todos"].update(values=todos)
            Todo_Functions.write_todos(todos)
        case "Edit":
            edit_todo = Values["Todos"][0]
            new_todo = Values['Todo']
            
            todos = Todo_Functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            
            Todo_Functions.write_todos(todos)
            Window["Todos"].update(values=todos)
        case 'Todos':
            Window["Todo"].update(value=Values["Todos"][0])
            
        case PySGUI.WIN_CLOSED:
            break   
            

Window.close()



