import PySimpleGUI as sg
from functions import feet_to_meters

label_feet = sg.Text('Feet: ')
input_box_feet = sg.InputText(tooltip='Input feet', key='feet_reading')
label_inches = sg.Text('Inches: ')
input_box_inches = sg.InputText(tooltip='Input Inches', key='inches_reading')
convert_button = sg.Button('Convert')
output_label = sg.Text('', key='output')

window = sg.Window('Convert to meters', layout=[[label_feet, input_box_feet],
                                                [label_inches, input_box_inches],
                                                [convert_button, output_label]])

while True:
    event, values = window.read()
    feet = float(values['feet_reading'])
    inches = float(values['inches_reading'])
    calc = feet_to_meters(feet, inches)
    window['output'].update(value=f'You are {round(calc,2)} meters', text_color='white')

window.close()