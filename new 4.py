from tkinter import *
from Banco import *
from Tela_Cadastrar_Nota import *
from gridview import Table
import sys

try:
    from Tkinter import Frame, Label, Message, StringVar
    from Tkconstants import *
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk
    from tkinter import Frame, Label, Message, StringVar
    from tkinter.constants import *

root = Tk()
notas = Notas_Usuario("4")
table = Table(root, ["Código Nota", "Usuário", "Título","Descrição", "Data"])
table.pack(expand=True,fill=X, padx=10,pady=10)


#table.set_data([[1,2,3,4],[4,5,6,7], [7,8,9,10], [10,11,12,13]])
table.set_data(notas)
#table.cell(0,1, " a fdas fasd fasdf asdf asdfasdf asdf asdfa sdfas asd sadf ")


root.mainloop()
