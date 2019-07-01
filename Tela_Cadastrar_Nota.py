from tkinter import *
from Banco import *

def Tela_Cadastrar_Nota(usuario):
	def Insere():
		titulo=Entry_Titulo.get()
		descricao=Entry_Descricao.get()
		Insere_Nota(usuario, titulo, descricao)
	
	janela = Tk()
	janela.geometry("250x250+250+250")
	
	Label_Titulo = Label(janela, text="Título: ")
	Label_Titulo.place(x=10, y=35)
	
	Label_Descricao = Label(janela, text="Descrição: ")
	Label_Descricao.place(x=10, y=60)
	
	Entry_Titulo = Entry(janela)
	Entry_Titulo.place(x=70, y=35)
	
	Entry_Descricao = Entry(janela)
	Entry_Descricao.place(x=70, y=60)
	
	
	
	botao_Cadastrar = Button(janela, width=20,text="Cadastrar", command = Insere)
	botao_Cadastrar.place(x=50, y=100)
	
	
	
	