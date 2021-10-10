import modulos as md
import pyautogui
import pyperclip
from time import sleep
import pandas as pd
from modulos.moeda import moedabr


pyautogui.PAUSE = 1.5

#abrir o google
pyautogui.press('win')
pyautogui.write('chr')
pyautogui.press('enter')

#ir até o site
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#baixar o arquivo
sleep(2)
pyautogui.doubleClick(x=380, y=357)
sleep(2)
pyautogui.click(x=384, y=431, button='right')
sleep(2)
pyautogui.click(x=547, y=938)

#abrir a planilha
sleep(3)
tabela = pd.read_excel(r'C:\Users\Lucas\Downloads\Vendas - Dez.xlsx')
faturamentoFinal = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(f'O faturamento deu {moedabr(faturamentoFinal)} e a quantidade de produtos vendidos foi {quantidade}')

#abrir o google
sleep(2)
pyautogui.press('win')
pyautogui.write('chr')
pyautogui.press('enter')

#enviar para o e-mail
pyperclip.copy('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
pyautogui.click(x=79, y=251)
sleep(2)
pyautogui.write('lucasptcastro@gmail.com')
pyautogui.press('tab')
sleep(2)
pyautogui.press('tab')

#corpo do e-mail
pyperclip.copy('Relatório de vendas 09/21')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
sleep(2)
texto = fr'''Equipe SuplementosVirtuais, bom dia!

Segue abaixo o relatório de vendas referente ao mês 09/21
O faturamento fechou em: {moedabr(faturamentoFinal)}
Foram vendidos {quantidade} produtos!

Atenciosamente, 
Lucas Peixoto

'''
pyautogui.write(texto)
pyautogui.hotkey('ctrl', 'enter')
