import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo')
add_button = sg.Button("Add")

# [[label], [input_box]] means the one element will exist underneath the other
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()

