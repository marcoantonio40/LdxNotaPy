from tkinter import *
from func_botao import bt_click


janela = Tk()

botao = Button(janela, width=20,text="OK", command=bt_click)
botao.place(x=100, y=100)

texto = Label(janela, text="Marco")
texto.place(x=100, y=150)

janela.geometry("300x300+200+200")
janela.mainloop()