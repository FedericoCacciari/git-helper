import PySimpleGUI as psg
import GUI.Functions as fs
useful_list = ["Copia repository", "Cambia Branch", "Aggiorna Repository", "Resetta Repository","Push repository"] 
dicta = {"Copia repository":"cp.repo", "Cambia Branch": "ch.Branch", "Aggiorna Repository":"up.repo","Resetta Repository":"rs.repo", "Push repository":"ps.repo"}

layout =[   [psg.Text("Git - Helper GUI")],
            [psg.Button("Copia repository"),
            psg.Button("Cambia Branch"),
            psg.Button("Aggiorna Repository"),
            psg.Button("Resetta Repository"),
            psg.Button("Push repository")],
            [psg.Button("Exit")]]


window = psg.Window("Gui - helper", layout)

def if_function(todo):
    if todo == "cp.repo":
        fs.cp_copy()
    if todo == "ch.Branch":
        fs.ch_branch()
    
while True:
    event, values = window.read()
    if event in useful_list:
        todo = dicta[event]
        if_function(todo)
    elif event == psg.WIN_CLOSED or "Exit":
        exit(0)