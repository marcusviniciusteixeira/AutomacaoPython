##*Fora do loop*
#Ir para a para do APP(Fora do loop)
##*Dentro do loop*
#Executar APP
#Esperar nevegador abrir(3 segundos)
#Colocar dados(Usuário/ Senha)
#Colocar número
#TOKEN
#Iniciar APP
#LOOP
#pyautogui.press('enter')

import pyautogui
import time

usuario = 'OEMNU'
senha = 'Pjfa#412'
num = '61991199657'

moveUsuario = 1200,300
moveSenha = 1200,300
moveNum = 1200,300
#sleep
appEnavegador = 1
logEnum = 1
numEtoken = 1

msg = 'Pressione OK para executar o programa.(OBS: Durante a execução não use o computador)'
winAcesso = 'documentos: Capturas de tela'

def Automacao():
    #Entrar pasta
    pyautogui.alert(msg)
    pyautogui.PAUSE = 0.5#PAUSEGERAL
    pyautogui.press('winleft')
    pyautogui.write(winAcesso)#Pasta ínicio execução
    pyautogui.moveTo(x=516, y=325)
    pyautogui.click()


    #pyautogui.press('winleft')
    #pyautogui.write('MACRO Portal Claro')#LOCAL PASTA
    
    for i in range(1,6):
        pyautogui.press('enter')
        time.sleep(appEnavegador)
        pyautogui.moveTo(moveUsuario)#USUÁRIO
        pyautogui.click()
        pyautogui.write(usuario)
        pyautogui.moveTo(moveSenha)#SENHA
        pyautogui.click()
        pyautogui.write(senha)
        time.sleep(logEnum)
        pyautogui.moveTo(moveNum)#NUM
        pyautogui.click()
        pyautogui.write(num)
        time.sleep(numEtoken)
        
Automacao()


