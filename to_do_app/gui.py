import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button("Add", size=10)
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos', enable_events=True,
                      size=[45, 10])
edit_button = sg.Button('Edit')

# [[label], [input_box, add_button]] means the one element will exist underneath the other
window = sg.Window('My To-Do App',
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, delete_button], [exit_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    '''could also do the below
    event = window.read()
    print(event[1]["todo"])'''
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 10))

        case "Delete":

            try:
                todo_to_delete = values['todos'][0]

                todos = functions.get_todos()
                index = todos.index(todo_to_delete)
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except:
                sg.popup('Please select an item first', font=('Helvetica', 10))


        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()

