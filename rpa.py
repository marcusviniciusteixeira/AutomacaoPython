import os
import pyautogui
import time

usuario = 'BW169'#BW169
#bw169
senha = 'OKM94ijn@'#
#okm94IJN@
numero = '61995843256'#61992255174

#SEGUNDOS ATE A TELA DO LOGIN
time1 = 13
#SEGUNDOS ATE A TELA DO LOGIN PARA A SENHA
time2 = 1.5

#i = 0
#for i in range(1,31OEMNU    Pjfa#412):
    #pyautogui.alert('Pressione OK para executar o programa.(OBS: Durante a execução não use o computador)')
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
pyautogui.write(numero)
pyautogui.moveTo(683, 505)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(576, 437)
pyautogui.click()

    #time1 =+ 0.3

    #if i == 10:
        #time1 + 3
    #if i == 15:
        #time1 + 3
    #if i == 20:
        #time1 + 3
