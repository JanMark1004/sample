import PySimpleGUI as sg


ui =[     [sg.Text("Goal Tracker")],
        [sg.Text('Enter Your Goal: '), 
        sg.InputText()],
        [sg.Button('Continue'), sg.Button('Cancel')]
    ]

class input_text:
    def __init__(self, input_text):
        self.input_text=input_text

text=input_text(sg.InputText)

window = sg.Window('Test').Layout(ui)

while True:


    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Continue':
        sg.popup('Thank You!')
        
    if event == 'Cancel':
        sg.popup('Goodbye')

window.Close()