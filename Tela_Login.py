from tkinter import *
from func_botao import bt_click_Entrar
from func_botao import bt_click_Sair
from func_botao import bt_click_Criar_Usu


janela = Tk()

texto = Label(janela, text="LdxNota")
texto.place(x=100, y=10)

Entry_Login = Entry().pack()
Entry_Senha = Entry().pack()

botao_Entrar = Button(janela, width=20,text="Entrar", command = bt_click_Entrar)
botao_Entrar.place(x=50, y=100)

botao_Criar_Usu = Button(janela, width=20,text="Entrar", command = bt_click_Criar_Usu)
botao_Criar_Usu.place(x=50, y=130)

botao_Sair = Button(janela, width=20, text="Sair", command = quit)
botao_Sair.place(x=50, y=160)



janela.geometry("250x250+250+250")
janela.mainloop()
