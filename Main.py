def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input('Type add,show, edit, complete or exit: ')
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
                
        todos.append(todo + "\n")
            
        with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
    elif user_action.startswith("show"):
        
        todos = get_todos()
                
        for index, items in  enumerate(todos):
                items = items.strip('\n')
                row = f'{index + 1}-{items}'
                print(row)
                
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1 
                
            todos = get_todos()
            
            new_todo = input('Enter a new Todo: ')
            todos[number] = new_todo +'\n'
                
            with open('todos.txt', 'w') as file:
                    file.writelines(todos)
        except ValueError:
            print("Your command is not Valid.")
            continue  
        except IndexError:
            print("That item is outside the list range.")
            continue        
            
    elif user_action.startswith("complete"):
        try:    
            number = int(user_action[9:])
                
            todos = get_todos()
                
            index = number - 1
            removed_todo = todos[index].strip('\n')
            todos.pop(index)
        
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                    
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

