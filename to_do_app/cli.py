import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f'It is {now}')

while True:
    user_action = input('Type add, show, edit, remove or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            # Will remove the space between the items
            item = item.strip('\n')
            row = f'{index + 1}: {item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input('Enter the new todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('remove'):
        try:
            number = int(user_action[7:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo: "{todo_to_remove}" was removed from the list.'
            print(message)

        except:
            print('Your command is not valid!')
            continue

    elif 'exit' in user_action:
        break

    else:
        print('Hey, you entered an unknown command')

print('Bye!')
