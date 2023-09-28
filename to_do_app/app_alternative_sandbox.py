def read_func():
    with open('list.txt', 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


should_continue = True

while should_continue:
    action = input('Type "add" to add, "show" to see the list, '
                   '"edit" to make an edit,'
                   '"remove" to remove or '
                   '"exit" to exit? ').strip().lower()

    if action == 'add':

        item_to_add = input('What do you want added? ')

        todo = read_func()

        todo.append(item_to_add + '\n')

        with open('list.txt', 'w') as file:
            file.writelines(todo)

    elif action == 'show':

        todo = read_func()

        for index, item in enumerate(todo):
            item = item.strip('\n')
            row = f'{index+1}: {item}'
            print(row)

    elif action == 'remove':
        num_to_remove = int(input('Which number would you like to remove? '))
        num_to_remove -= 1

        todo = read_func()

        items_to_remove = todo[num_to_remove]
        todo.pop(num_to_remove)

        with open('list.txt', 'w') as file:
            file.writelines(todo)

        print(f'You have successfully removed {items_to_remove}')


    elif action == 'edit':
        num_to_edit = int(input('Which number would you like to edit? '))
        num_to_edit -= 1

        todo = read_func()

        new_entry = input('What is the new item? ')
        todo[num_to_edit] = new_entry + '\n'

        with open('list.txt', 'w') as file:
            file.writelines(todo)

    else:
        should_continue = False

print('See ya later alligata!')


