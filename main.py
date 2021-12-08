import pyautogui
import time

def Automacao():
    pyautogui.alert('O código está sendo executado. Não mexa!')
    pyautogui.PAUSE = 0.5#PAUSEGERAL
#Área de Trabalho
#Entrar pasta
    #pyautogui.press('winleft')
    #pyautogui.write('MACRO Portal Claro')#LOCAL PASTA
    for i in range(1,6):
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.moveTo(1200,300)#USUÁRIO
        pyautogui.click()
        pyautogui.write('OEMNU')
        pyautogui.moveTo(1200,300)#SENHA
        pyautogui.click()
        pyautogui.write('Pjfa#412')
        time.sleep(0.5)
        pyautogui.moveTo(1200,300)#NUM
        pyautogui.click()
        pyautogui.write('61991199657')
        time.sleep(1)

Automacao()
    

#Executar APP
#Esperar nevegador abrir(3 segundos)
#Colocar dados(Usuário/ Senha)
#Colocar número
#TOKEN
#Iniciar APP
#LOOP
#pyautogui.press('enter')

