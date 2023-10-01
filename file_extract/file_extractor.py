import PySimpleGUI as sg
from functions import extract_archive

sg.theme("Black")

label1 = sg.Text('Select and Archive')
input1 = sg.Input()
choose_button = sg.FileBrowse('Choose', key='archive')

label2 = sg.Text('Select a destination')
input2 = sg.Input()
dest_button = sg.FileBrowse('Destination', key='folder')

extract_button = sg.Button('Extract')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('File Extractor',
                   layout=[[label1, input1, choose_button],
                           [label2, input2, dest_button],
                           [extract_button, output_label]])

while True:
    event,values = window.read()
    print(event, values)
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window['output'].update(value='Extract complete!')

window.close()
