import PySimpleGUI as psg

psg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [psg.Text('Some text on Row 1')],
            [psg.Text('Enter something on Row 2'), psg.InputText()],
            [psg.Button('Ok'), psg.Button('Cancel')] ]

# Create the Window
window = psg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
print(type(layout))