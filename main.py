import PySimpleGUI as sg
import os
import time
import pyautogui

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

    def Iniciar(self):
        usuario = self.values['usuario']
        senha = self.values['senha']
        num = self.values['num']
        time1 = self.values['time1']
        time2 = self.values['time2']
        os.startfile('PortalClaro.exe')
        time.sleep(time1)
        pyautogui.moveTo(571, 409)#USUÁRIO
        pyautogui.click()
        pyautogui.write(usuario)
        pyautogui.press('tab')#SENHA
        pyautogui.write(senha)#Pjfa#412
        pyautogui.moveTo(672, 530)
        pyautogui.click()
        time.sleep(time2)
        pyautogui.moveTo(556, 472)#NUM
        pyautogui.click()
        pyautogui.write(num)
        pyautogui.moveTo(683, 505)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(576, 437)
        pyautogui.click()



tela = TelaPython()
tela.Iniciar()