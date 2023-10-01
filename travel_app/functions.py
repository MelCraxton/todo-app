def open_items():
    with open('items.txt', 'r') as file:
        current_items = file.readlines()
        return current_items


def write_items(current_items):
    with open('items.txt', 'w') as file:
        file.writelines(current_items)


