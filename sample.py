import PySimpleGUI as sg

sg.theme('DarkAmber')   

layout = [  [sg.Text('足し算')],
            [sg.Text('数１'), sg.InputText()],
            [sg.Text('数２'), sg.InputText()],
            [sg.Text('0',key='ans'), ],
            [sg.Button('計算'), sg.Button('Cancel')] ]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    
    if event == '計算':
        num1 = int(values[0])
        num2 = int(values[1])
        window['ans'].update(str(num1+num2))
        #sg.popup(num1 + num2)

window.close()
