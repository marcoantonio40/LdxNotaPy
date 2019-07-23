from tkinter import *
from Banco import Insere_Usuario
import ctypes 

def Tela_Cadastra():
	def Limpa_Entry():
		Entry_Nome_Usu.delete(first=0,last=50)
		Entry_Login_Usu.delete(first=0,last=50)
		Entry_Senha_Usu.delete(first=0,last=50)
		Entry_Senha_Confirma.delete(first=0,last=50)
		
	janela = Tk()
	
	texto_titulo = Label(janela, text="LdxNota - Cadastra Usuários")
	texto_titulo.place(x=50, y=10)
	
	Label_Nome_Usu = Label(janela, text="Nome: ")
	Label_Nome_Usu.place(x=50, y=50)

	Label_Login_Usu = Label(janela, text="Login: ")
	Label_Login_Usu.place(x=50, y=75)

	Label_Senha_Usu = Label(janela, text="Senha: ")
	Label_Senha_Usu.place(x=50, y=100)
	
	Label_Senha_Confirma = Label(janela, text="Confirma: ")
	Label_Senha_Confirma.place(x=32, y=125)

	Entry_Nome_Usu = Entry(janela)
	Entry_Nome_Usu.place(x=90, y=50)

	Entry_Login_Usu = Entry(janela)
	Entry_Login_Usu.place(x=90, y=75)

	Entry_Senha_Usu = Entry(janela, show = '*')
	Entry_Senha_Usu.place(x=90, y=100)
	
	Entry_Senha_Confirma = Entry(janela, show = '*')
	Entry_Senha_Confirma.place(x=90, y=125)
	
	def fechar_Janela():	
		janela.destroy()
	
	def Confere_Senha(senha1, senha2):
		if(senha1 == senha2):
			return True
		else:
			return False
		
		
	def Insere():
		nome = Entry_Nome_Usu.get()
		login = Entry_Login_Usu.get()
		senha1 = Entry_Senha_Usu.get()
		senha2 = Entry_Senha_Confirma.get()
		if(Confere_Senha(senha1, senha2)):
			Insere_Usuario(nome, login, senha1)
			Limpa_Entry()
		else:
			ctypes.windll.user32.MessageBoxW(0, "Senhas diferentes", "Erro", 0)
		
		

	botao_Cadastrar_Usu = Button(janela, width=20,text="Cadastrar", command = Insere)
	botao_Cadastrar_Usu.place(x=50, y=150)

	botao_Voltar_Usu = Button(janela, width=20,text="Sair", command = fechar_Janela)
	botao_Voltar_Usu.place(x=50, y=180)

	janela.geometry("250x250+550+250")
	janela.mainloop()
