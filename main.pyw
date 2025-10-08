import os
from pynput.keyboard import Controller, Key
import dearpygui.dearpygui as dpg
from time import sleep
import sys

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

def btn_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    if (sender == "numbers"):
        send(numbers + numbers_pt)
    elif (sender == "seculos"):
        send(roman_numerals)
    elif (sender == "months"):
        send(months)
    elif (sender == "verbs"):
        send(roman_numerals)
    elif (sender == "primeira"):
        send(ordinals)
    elif (sender == "alph"):
        send(alphabet)
    elif (sender == "time"):
        send(time_units)
    elif (sender == "fim"):
        send(fim)
    elif (sender == "exit"):
        exit()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def typewrite(txt):
    for i in txt:
        keyboard.type(i)
        sleep(0.0015)

def send(arr):
    print("     Starting in: ")
    dpg.set_value(1, "Starting in: ")
    for i in range(3):
        dpg.set_value(1, f"Starting in: {3-i}")
        print(3-i)
        sleep(1)
    for i in arr:
        typewrite(i)
        keyboard.tap(Key.enter)
        sleep(0.1)
    dpg.set_value(1, "Ready...")

dpg.create_context()
dpg.create_viewport(title='Artigo-Helper', width=480, height=100)
dpg.setup_dearpygui()
btnw=110

with dpg.font_registry():
    default_font = dpg.add_font(resource_path("SpaceMono-Regular.ttf"), 22)
with dpg.window(label="Artigo Helper", tag="primary"):
    with dpg.group(horizontal=True):
        with dpg.group():
            dpg.add_text("Artigo helper made with love and GPT")
            dpg.add_text("Ready...", id=1, tag="out")
        dpg.add_text(""" ,-"-,-"-.
(         )
 ".     ."
   "._." """, color=[255,0,0])
    with dpg.group(horizontal=True):
        dpg.add_button(width=btnw, label="Numbers", tag="numbers", callback=btn_callback)
        dpg.add_button(width=btnw, label="Séculos", tag="seculos", callback=btn_callback)
        dpg.add_button(width=btnw, label="Months", tag="months", callback=btn_callback)
    with dpg.group(horizontal=True):
        dpg.add_button(width=btnw, label="Verbos", tag="verbs", callback=btn_callback)
        dpg.add_button(width=btnw, label="Primeira", tag="primeira", callback=btn_callback)
        dpg.add_button(width=btnw, label="Alphabet", tag="alph", callback=btn_callback)
    with dpg.group(horizontal=True):
        dpg.add_button(width=btnw, label="Timeunits", tag="time", callback=btn_callback)
        dpg.add_button(width=btnw, label="Fim", tag="fim", callback=btn_callback)
        dpg.add_button(width=btnw, label="Exit", tag="exit", callback=btn_callback)
    dpg.bind_font(default_font)

dpg.show_viewport()
dpg.set_primary_window("primary", True)
dpg.start_dearpygui()
dpg.destroy_context()




def legacy_unwindowed():
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


