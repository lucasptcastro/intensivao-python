import pyautogui
from time import sleep
from modulos.moeda import *

#sleep(5)
#print(pyautogui.position())

def moedabr(n, format=True):
    if format == False:
        return n
    else:
        a = f'{float(n):,.2f}'
        b = a.replace(',','v')
        c = b.replace('.',',')
        return f'R${c}'.replace('v','.')


print(moedabr('52352'))