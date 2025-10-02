#from pyautogui import press, typewrite, hotkey
from pynput.keyboard import Controller, Key
from time import sleep 

keyboard = Controller()

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers_pt = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa", "cem", "cento", "mil", "milhão", "bilhão"]
roman_numerals = ["século", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi"]
common_verbs = ["ser", "estar", "ter", "fazer", "poder", "dizer", "ir", "ver", "dar", "saber"]
months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

ordinals = ["primeira", "segunda", "terceira", "quarta", "quinta", "sexta", "sétima", "oitava", "nona", "décima", "última"]
time_units = ["hora", "dia", "minuto", "segundo", "semana", "mês", "ano", "década", "século", "milênio"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
fim = ["começar", "começo", "início", "iniciar", "fim", "final", "finalizar", "meio", "metade"]



def typewrite(txt):
    for i in txt:
        keyboard.type(i)
        sleep(0.0015)

def send(arr):
    print("     Starting in: ")
    for i in range(3):
        print(3-i)
        sleep(1)
    for i in arr:
        typewrite(i)
        keyboard.tap(Key.enter)
        sleep(0.1)


print(r'''
      ______________________________________________
      |                                            |
      |  Artigo helper made with love and ChatGPT  |
      |____________________________________________|

             ,-"-,-"-.
            (         )
             ".     ."
               "._." 
                     _  _
                    ( `' )
                     `.,'
         ,-.-.
         `. ,'
           `

      ''')
while (True):
    a = input(r'''
      ____________________________________________________________
      | Press: |    1    |    2    |    3    |    4    |    5    |
      |        |         |         |         |         |         |
      |  for:  | numbers | séculos |  months |  verbs  |primeira |
      |________|_________|_________|_________|_________|_________|
      | Press: |    6    |    7    |    8    |    9    |    0    |
      |        |         |         |         |         |         |
      |  for:  |alphabet |timeunits|   fim   |         |  close  |
      |________|_________|_________|_________|_________|_________|

        Select: ''')
    if (a == "1"):
        send(numbers + numbers_pt)
    elif (a == "2"):
        send(roman_numerals)
    elif (a == "3"):
        send(months)
    elif (a == "4"):
        send(common_verbs)
    elif (a == "5"):
        send(ordinals)
    elif (a == "6"):
        send(alphabet)
    elif (a == "7"):
        send(time_units)
    elif (a == "8"):
        send(fim)
    elif (a == "9"):
        send(["I love You"])
    elif (a == "0"):
        exit()
    else:
        print("Ungültiger input, try novamente. ")


