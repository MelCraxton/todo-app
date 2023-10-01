from functions import open_items, write_items

add_to_list = True

while add_to_list:

    user_input = input('What would you like to do with your travel list? '
                       'Type "add", "show", "remove", "edit" or "exit": ').strip().lower()

    # user_input = user_input.strip()

    if user_input == 'add':

        item = input('What would you like to add? ')

        current_items = open_items()

        current_items.append(item + '\n')

        write_items(current_items)

    elif user_input == 'show':

        current_items = open_items()

        for index, item in enumerate(current_items):
            item = item.strip('\n')
            index = index + 1
            print(index, item)

    elif user_input == 'edit':

        item_to_edit = int(input('Please choose the number you want to edit: '))
        new_item = input('What would you like to add? ')
        item = item_to_edit - 1

        current_items = open_items()

        current_items[item] = new_item + '\n'

        write_items(current_items)

        print(f'You have successfully replaced item {item_to_edit} with {new_item}')

    elif user_input == 'remove':

        try:
            item_to_delete = int(input('Which number item would you like to delete? '))
            item = item_to_delete - 1
            print(item)

            current_items = open_items()

            item_to_remove = current_items[item].strip('\n')
            print(item_to_remove)
            current_items.pop(item)

            write_items(current_items)

            print(f'You have successfully removed {item_to_remove}')

        except:
            print('Please input a number')
            continue

    elif user_input == "exit":
            print('See ya!')
            add_to_list = False

    else:
        print('Sorry I do not understand, please try again?')

