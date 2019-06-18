from tkinter import *
from Banco import Insere_Usuario



def Tela_Cadastra():
	janela = Tk()
	
	texto_titulo = Label(janela, text="LdxNota - Cadastra Usuários")
	texto_titulo.place(x=50, y=10)
	
	Label_Nome_Usu = Label(janela, text="Nome: ")
	Label_Nome_Usu.place(x=50, y=50)

	Label_Login_Usu = Label(janela, text="Login: ")
	Label_Login_Usu.place(x=50, y=75)

	Label_Senha_Usu = Label(janela, text="Senha: ")
	Label_Senha_Usu.place(x=50, y=100)

	Entry_Nome_Usu = Entry(janela)
	Entry_Nome_Usu.place(x=90, y=50)

	Entry_Login_Usu = Entry(janela)
	Entry_Login_Usu.place(x=90, y=75)

	Entry_Senha_Usu = Entry(janela)
	Entry_Senha_Usu.place(x=90, y=100)
	
	nome=Entry_Nome_Usu.get()
	login=Entry_Login_Usu.get()
	senha=Entry_Senha_Usu.get()

	botao_Cadastrar_Usu = Button(janela, width=20,text="Cadastrar", command = Insere_Usuario(nome, login, senha))
	botao_Cadastrar_Usu.place(x=50, y=140)

	botao_Voltar_Usu = Button(janela, width=20,text="Voltar", command = print("Voltar"))
	botao_Voltar_Usu.place(x=50, y=170)

	
	janela.geometry("250x250+250+250")
	janela.mainloop()
