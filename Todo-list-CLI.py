from Modules import Todo_Functions  
import time 

current_time = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", current_time)

while True:
    user_action = input('Type add,show, edit, complete or exit: ')
    user_action = user_action.strip()
       
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = Todo_Functions.get_todos()
                
        todos.append(todo + "\n")
        
        Todo_Functions.write_todos(todos)
    elif user_action.startswith("show"):
        
        todos = Todo_Functions.get_todos()
                
        for index, items in  enumerate(todos):
                items = items.strip('\n')
                row = f'{index + 1}-{items}'
                print(row)
                
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1 
                
            todos = Todo_Functions.get_todos()
            
            new_todo = input('Enter a new Todo: ')
            todos[number] = new_todo +'\n'
            
            Todo_Functions.write_todos(todos)      
        except ValueError:
            print("Your command is not Valid.")
            continue  
        except IndexError:
            print("That item is outside the list range.")
            continue        
            
    elif user_action.startswith("complete"):
        try:    
            number = int(user_action[9:])
                
            todos = Todo_Functions.get_todos()
                
            index = number - 1
            removed_todo = todos[index].strip('\n')
            todos.pop(index)
            
            Todo_Functions.write_todos(todos) 
            
            message = f'Todo {removed_todo} was completed and removed from the list.'
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not Valid.")
            continue        
    elif user_action.startswith("exit"):
        break
    else:
        print('Wrong Input Recieved')
    
    
print('Finished')

