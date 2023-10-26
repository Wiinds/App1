todos = []

while True:
    user_action = input('Type add,show, edit, complete or exit: ')
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a Todo: ')
            todos.append(todo)
        case 'show':
            for index, items in  enumerate(todos):
                row = f'{index + 1}-{items}'
                print(row)
                #items = items.title()
                #print(index,'-', items)
        case 'edit':
            number = int(input('Number of the Todo item to Edit: ')) 
            number = number - 1 
            new_todo = input('Enter a new Todo: ')
            todos[number] = new_todo
        case 'complete':
            number = int(input('Enter the Number of the Completed item to remove: '))
            todos.pop(number - 1)
        case 'exit':
            break
        case _ :
            print('Wrong Input Recieved')
    
    
print('Finished')

