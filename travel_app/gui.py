import functions
import PySimpleGUI as sg

sg.theme("Purple")

label = sg.Text("Its time to travel! \nType in an item you will need for your trip")
input_box = sg.InputText(tooltip='Enter travel item', key='travel_item')
add_button = sg.Button('Add', size=10)
edit_button = sg.Button('Edit')
delete_button = sg.Button('Delete')
exit_button = sg.Button('Exit')


list_box = sg.Listbox(values=functions.open_items(), key='current_travel_list',
                      enable_events=True, size=[45,10])

window = sg.Window('My Travel App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button, delete_button],
                           [exit_button]],
                   font=('Helvetica', 10))

while True:
    # This calls the window to be displayed on the screen,
    # we can store it in a variable and it also records what a user types in
    # The search box and returns the name of the button that was pressed and the user input
    event, values = window.read()
    print(event)
    print(values)
    print(values['current_travel_list'])
    # print(values['current_travel_list'][0])

    match event:
        case 'Add':
            current_items = functions.open_items()
            new_travel_item = values['travel_item'] + "\n"
            current_items.append(new_travel_item)
            functions.write_items(current_items)
            # This will update the list_box in real time with the value that the user inputs into the input_box
            window['current_travel_list'].update(values=current_items)

        case 'Edit':

            try:
                # Get the item that is to be edited
                item_to_edit = values['current_travel_list'][0]
                # Gets the new entry from the 'travel_item' key
                new_travel_item = values['travel_item']

                # Runs the open_items() function
                current_items = functions.open_items()
                # Get the index of the current_items, and the item that
                #  is to be edited
                index = current_items.index(item_to_edit)
                # That item at that index will be replaced with the new travel item
                current_items[index] = new_travel_item
                # This will update the list with the new item
                functions.write_items(current_items)
                # This will then update the list_box in real time
                window['current_travel_list'].update(values=current_items)

            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 10))

        case 'Delete':

            try:
                item_to_delete = values['current_travel_list'][0]
                print(item_to_delete)
                current_items = functions.open_items()
                index = current_items.index(item_to_delete)
                current_items.pop(index)
                functions.write_items(current_items)
                window['current_travel_list'].update(values=current_items)

            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 10))

        case 'Exit':
            break

        # This will update the input_box with what the user clicks on
        #  In the list box
        case 'current_travel_list':
            window['travel_item'].update(value=values['current_travel_list'][0])

        # Helps the program to shut correctly when clicking
        # The close button
        case sg.WIN_CLOSED:
            break
window.close()
