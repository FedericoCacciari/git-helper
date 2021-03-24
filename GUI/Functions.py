import PySimpleGUI as psg
from pathlib import Path
from Files import git_helper as gh
import time

def cp_copy():
    psg.theme('DarkAmber')
    layout = [[psg.Text("Copy Repository")],
              [psg.Text("Insert Link:"), psg.InputText(key="in_text")], 
              [psg.Text("Current Dir = "),psg.Text(Path.cwd(), key="dir")], 
              [psg.FolderBrowse(key="Browse")],
              [psg.Text("Modalità forzata: "), psg.Button('Off', size=(3,1), button_color=('white', 'red'), key='_B_')],
              [psg.Button("Exit"),psg.Button("OK")]]

    window = psg.Window("Copy Repository - Git Helper", layout)

    down = False

    while True:
        events, values = window.read()
        print(values["Browse"])
        if values["Browse"] != "":
            window.Element("dir").update(values["Browse"])
            window.refresh()
        if events == '_B_':
            down = not down
            window.Element('_B_').Update(('Off','On')[down], button_color=(('white', ('red', 'green')[down])))
        if events == "OK":
            chosen_dir = values["Browse"]
            link = values["in_text"]
            break
        if events == "Exit" or events == psg.WIN_CLOSED:
            exit(0)


    window.close()
    
    try:
        if chosen_dir == "":
            chosen_dir = Path.cwd()
        else:
            chosen_dir = Path(chosen_dir)
    except:
        chosen_dir = Path.cwd()
    try:
        gh.clone_repo(link, chosen_dir, down)
        done()
    except:
        error()

def error():
    layout = [[psg.Text("L'url non è stato inserito correttamente, rifare")], [psg.Button("OK"),psg.Button("Annulla")]]
    window = psg.Window("Errore", layout)
    
    check = True
    if check == True:
        event = window.read()
        if event == "OK" or event == psg.WIN_CLOSED:
           check = False
        if event == "Annulla":
            exit()
    
    window.close()
    cp_copy()

def done():
    layout = [[psg.Text("Done")]]
    window = psg.Window("Done", layout)
    while True:
        event = window.read()
        if event == psg.WIN_CLOSED:
            break
    window.close()
    exit(0)

    