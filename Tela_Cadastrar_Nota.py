from tkinter import *
from Banco import *


def Tela_Cadastrar_Nota(usuario):
	def Limpa_Entry():
		Entry_Descricao.delete(first=0,last=200)
		Entry_Titulo.delete(first=0,last=50)	
	
	def Insere():
		titulo=Entry_Titulo.get()
		descricao=Entry_Descricao.get()
		Entry_Titulo.insert(0,"")
		Entry_Descricao.insert(0,"")
		Insere_Nota(usuario, titulo, descricao)
		Limpa_Entry()
	
	janela = Tk()
	janela.geometry("250x250+550+250")
	
	texto = Label(janela, text="LdxNota - Cadastrar Notas")
	texto.place(x=60, y=10)
	
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
	
	
	
	