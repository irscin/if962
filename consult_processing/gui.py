from tkinter import *
import pandas as pd
from general_query import GeneralQuery
import os
import json

root = Tk()
root.geometry("500x700")
root.resizable(0, 0)

text = Text(root)

def getGames():
    query = GeneralQuery(eGame.get().lower(), eDesc.get().lower(), eOS.get().lower(), eRam.get().lower(), eStorage.get().lower(), ePrice.get().lower())
    result = query.processQuery()
    text.delete('1.0', END)
    #Display games informations
    for game in result:
        gamePath = os.path.abspath('../inverted_index/db/' + str(game[0]))

        jsonGame = None    
        with open(gamePath, 'r', encoding="unicode_escape") as fp:
            jsonGame = json.loads(fp.read()[0:-1])
        
        r = StringVar()
        print(jsonGame)
        text.insert(INSERT, (str("\nName: " + jsonGame["game"] + "\nPrice: " + jsonGame["price"] + "\nos: " + jsonGame["os"] + "\nram: " + jsonGame["ram"] + "\nstorage: " + jsonGame["storage"] + "\n")))
        #lResult = Label(frame, font=("Helvetica", 9),textvariable=r)
        text.pack()

lHead = Label(root, font=("Helvetica", 24), text="The Gamenator\n")
lHead.pack()

lGame = Label(root, text="\nNome do Jogo")
lGame.pack()
eGame = Entry(root)
eGame.pack()
eGame.focus_set()

lDesc = Label(root, text="\nDescrição")
lDesc.pack()
eDesc = Entry(root)
eDesc.pack()
eDesc.focus_set()

lOS = Label(root, text="\nOS")
lOS.pack()
eOS = Entry(root)
eOS.pack()
eOS.focus_set()

lRam = Label(root, text="\nRAM")
lRam.pack()
eRam = Entry(root)
eRam.pack()
eRam.focus_set()

lStorage = Label(root, text="\nArmazenamento")
lStorage.pack()
eStorage = Entry(root)
eStorage.pack()
eStorage.focus_set()

lPrice = Label(root, text="\nPreço")
lPrice.pack()
ePrice = Entry(root)
ePrice.pack()
ePrice.focus_set()

bGeral = Button(root, text="Pesquisar", command=getGames)
bGeral.pack()

lspace = Label(root, text="\nResultados:")
lspace.pack()

mainloop()