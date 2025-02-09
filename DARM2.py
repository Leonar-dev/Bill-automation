#Importando as bibliotecas pyaotogui e time
#Obs é necessario mudar o point do click de acordo com seu monitor (Resolução)
import pyautogui
import time

#Tempo de espera para todas as funções
pyautogui.PAUSE = 0.8

#Entrando no Google CHrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Clicando na Barra URL e entrando no link
pyautogui.click(x=592, y=307)
pyautogui.write("https://iportal.rio.rj.gov.br/PF302PARCISSINCPREDIAL/pages/PARCISSINCPREDIAL/MENUPARCISS.aspx")
pyautogui.press("enter")

#Clicando na opção Solicitar impressão 2ª via
pyautogui.scroll(-300)
pyautogui.click(x=652, y=501)

#Inserindo Inscrição municipal e Processo
pyautogui.scroll(-2000)
pyautogui.click(x=550, y=202)
pyautogui.write("digite a IE aqui")
pyautogui.press("tab")
pyautogui.write ("Digite o Processo aqui")
pyautogui.click(x=1009, y=438)

#Clicando no alerta "Enviar assim mesmo"
pyautogui.click(x=454, y=506)

#Tela para Impressão/Salva do boleto (Copia do Numero do boleto)
pyautogui.scroll(-2000)
pyautogui.moveTo(229, 333, duration=1) 
pyautogui.dragTo(256, 331, duration=1, button='left') 
pyautogui.hotkey('ctrl', 'c')

#Renomeando e salvando boleto
pyautogui.click(x=415, y=323)
pyautogui.press("enter")
pyautogui.write("Boleto")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")

#Fechando o Chrome
pyautogui.click(x=1326, y=23)



