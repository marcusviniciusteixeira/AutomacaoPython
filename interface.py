import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Usuário',size=(10,0)), sg.Input(size=(20,0),key='usuario')],
            [sg.Text('Senha',size=(10,0)), sg.Input(size=(20,0),key='senha')],
            [sg.Text('Número',size=(10,0)), sg.Input(size=(20,0),key='num')],
            [sg.Text('Time1',size=(10,0)), sg.Slider(range=(0,30), default_value=0, orientation='h',size=(10,15),key='time1')],
            [sg.Text('Time2',size=(10,0)), sg.Slider(range=(0,30), default_value=0, orientation='h',size=(10,15),key='time2')],
            [sg.Button('Executar')]
        ]

        janela = sg.Window("Macro Portal CLARO").layout(layout)

        self.button, self.values = janela.read()
